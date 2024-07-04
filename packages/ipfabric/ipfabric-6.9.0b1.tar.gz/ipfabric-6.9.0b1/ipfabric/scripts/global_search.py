"""
Python3 script to search for an IPv4, IPv6, or MAC address in multiple IP Fabric's tables and prints the output.
"""

import argparse
import json
import logging
import re
from copy import deepcopy
from typing import List, Dict, Union

from ipfabric import IPFClient
from ipfabric.models.global_search import GlobalSearch, RANKED
from ipfabric.tools.shared import valid_snapshot

try:
    from rich.console import Console

    CONSOLE = Console()
except ImportError:
    CONSOLE = None

logging.basicConfig(format="%(levelname)s: %(message)s")

LOGGER = logging.getLogger("ipf_global_search")


def main() -> Dict[str, Dict[str, Union[str, list]]]:
    arg_parser = argparse.ArgumentParser(
        description="Search all tables for an IPv4, IPv6, or MAC address. "
        "This does not include IPv4 or IPv6 Route tables as too many results would be returned.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=f"""
Tables are searched in the order as listed below.  If Full Scan option is enabled then any other tables are
printed after these results in no specific order.\n

Default Tables for IPv4 Search:
{chr(10).join([f'{idx + 1}. {_}' for idx, _ in enumerate(RANKED['ipv4'])])}
\n
Default Tables for IPv6 Search:
{chr(10).join([f'{idx + 1}. {_}' for idx, _ in enumerate(RANKED['ipv6'])])}
\n
Default Tables for MAC Search:
{chr(10).join([f'{idx + 1}. {_}' for idx, _ in enumerate(RANKED['mac'])])}
""",
    )
    arg_parser.add_argument(
        "address",
        help="IPv4, IPv6, or MAC address to search for.",
    )
    arg_parser.add_argument(
        "-f",
        "--full-scan",
        help="Scan all tables not just default.  It will take more time so it is "
        "recommended to use if first search could not locate anything.",
        action="store_true",
        default=False,
    )
    arg_parser.add_argument(
        "-r",
        "--regex",
        help="Perform a regex search instead of an exact match on the tables, please quote your regex.",
        choices=[
            "ipv4",
            "ipv6",
            "mac",
        ],
    )
    arg_parser.add_argument(
        "-c",
        "--count",
        help="Print count of rows instead of the actual data.",
        action="store_true",
        default=False,
    )
    arg_parser.add_argument(
        "-s",
        "--snapshot",
        help="Snapshot to use which can be a UUID or one of ['last', 'prev', 'lastLocked']"
        "with or without `$` for *nix compatability.",
        default="$last",
    )
    arg_parser.add_argument(
        "-v",
        "--verbose",
        help="Verbose output will enable debugging and print all tables even if no data.",
        action="store_true",
        default=False,
    )
    arg_parser.add_argument(
        "-j",
        "--json",
        help="Enable JSON output which will also print all tables even if no data.",
        action="store_true",
        default=False,
    )
    arg_parser.add_argument(
        "-R",
        "--rich-disable",
        help="Disable rich formatting if installed. Useful for sending JSON output to jq.",
        action="store_true",
        default=False,
    )
    args = arg_parser.parse_args()

    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)
        logging.getLogger("ipfabric").setLevel(logging.DEBUG)
        LOGGER.debug("Logging level set to DEBUG")

    if args.snapshot.lower() in ["last", "prev", "lastlocked"]:
        args.snapshot = "$" + args.snapshot
    args.snapshot = valid_snapshot(args.snapshot)
    LOGGER.debug(f"Snapshot ID selected: {args.snapshot}")
    ipf = IPFClient(snapshot_id=args.snapshot.strip("'"))
    gs = GlobalSearch(client=ipf)
    if args.regex:
        results = gs.search_regex(search_type=args.regex, address=args.address, full_scan=args.full_scan)
    else:
        results = gs.search(address=args.address, full_scan=args.full_scan)
    print_results(list(results.values()), args.address, args)


def bold_string(results: List[dict], address: str):
    regex = re.compile(rf"({address})")

    def bold_loop(result):
        if isinstance(result, list):
            for _ in result:
                bold_loop(_)
        elif isinstance(result, dict):
            for k, v in result.items():
                result[k] = bold_loop(v)
        elif isinstance(result, (str, bytes)):
            return regex.sub(r"[b u]\1[/b u]", result)
        return result

    return bold_loop(deepcopy(results))


def rich_print(result: dict, address: str, count: bool = False):
    CONSOLE.print(f"\n{result['menu']}: {str(len(result['data']))}" if count else f"\n{result['menu']}")
    CONSOLE.print(result["url"], style=f"link {result['url']}")
    if not count:
        json_str = json.dumps(bold_string(result["data"], address), indent=4)
        CONSOLE.print(json_str)


def py_print(result: dict, count: bool = False):
    print(f"\n{result['menu']}: {str(len(result['data']))}" if count else f"\n{result['menu']}")
    print(result["url"])
    if not count:
        print(json.dumps(result["data"], indent=4))


def print_json(results: dict, address: str):
    if CONSOLE:
        for result in results:
            result["data"] = bold_string(result["data"], address)
        CONSOLE.print(json.dumps(results, indent=4))
    else:
        print(json.dumps(results, indent=4))


def print_results(results: list, address: str, args: argparse.Namespace):
    global CONSOLE
    if args.rich_disable:
        CONSOLE = None
    verbose, full_scan, count = args.verbose, args.full_scan, args.count
    if not verbose and not [y for x in results for y in x["data"]]:
        msg = f'\nAddress "{address}" not found in tables'
        msg += "." if full_scan else ", try running with '-f|--full-scan' to query all tables."
        CONSOLE.print(msg) if CONSOLE else LOGGER.error(msg)
        exit(1)
    if args.json:
        print_json(results, address)
        return
    for result in results:
        if not result["data"] and not verbose:
            continue
        if CONSOLE:
            rich_print(result, address, count)
        else:
            py_print(result, count)


if __name__ == "__main__":
    main()
