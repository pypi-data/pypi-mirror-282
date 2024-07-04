import ipaddress
import json
import logging
from typing import List, Any, Union, Dict, Literal
from collections import OrderedDict

from macaddress import EUI48
from pydantic import BaseModel, Field, PrivateAttr

from ipfabric.models.oas import Endpoint, NestedColumn
from ipfabric.tools.shared import parse_mac

LOGGER = logging.getLogger("ipfabric")

VM_INTS = "/tables/cloud/virtual-machines-interfaces"
RANKED = {
    "ipv4": [
        "/tables/addressing/managed-devs",
        "/tables/inventory/interfaces",
        "/tables/addressing/hosts",
        "/tables/addressing/arp",
        "/tables/wireless/clients",
        "/tables/inventory/phones",
        VM_INTS,
        "/tables/neighbors/unmanaged",
        "/tables/interfaces/connectivity-matrix/unmanaged-neighbors/detail",
        "/tables/routing/protocols/bgp/neighbors",
        "/tables/routing/protocols/eigrp/neighbors",
        "/tables/routing/protocols/is-is/neighbors",
        "/tables/routing/protocols/ospf/neighbors",
        "/tables/routing/protocols/rip/neighbors",
    ],
    "ipv6": [
        "/tables/addressing/ipv6-managed-devs",
        "/tables/addressing/ipv6-hosts",
        "/tables/addressing/ipv6-neighbors",
        "/tables/neighbors/unmanaged",
        "/tables/interfaces/connectivity-matrix/unmanaged-neighbors/detail",
        VM_INTS,
        "/tables/routing/protocols/bgp/neighbors",
        "/tables/routing/protocols/is-is/neighbors",
        "/tables/routing/protocols/ospf-v3/neighbors",  # NIM-15216
    ],
    "mac": [
        "/tables/addressing/managed-devs",
        "/tables/addressing/ipv6-managed-devs",
        "/tables/inventory/interfaces",
        "/tables/addressing/hosts",
        "/tables/addressing/ipv6-hosts",
        "/tables/addressing/ipv6-neighbors",
        "/tables/addressing/arp",
        VM_INTS,
        "/tables/addressing/mac",
        "/tables/wireless/radio",
    ],
}


class GlobalSearch(BaseModel):  # TODO: CIDR and Route Table Searching, Stop after first match
    client: Any = Field(exclude=True)
    _ipv4: List[Endpoint] = PrivateAttr(default_factory=list)
    _ipv6: List[Endpoint] = PrivateAttr(default_factory=list)
    _mac: List[Endpoint] = PrivateAttr(default_factory=list)

    def model_post_init(self, __context: Any) -> None:
        self._load_default()
        self._load_dynamic()

    def _load_default(self):
        for k, v in RANKED.items():
            for path in v:
                if getattr(self.client.oas[path[1:]].post, k).columns:
                    getattr(self.client.oas[path[1:]].post, k).full_scan = False
                    getattr(self, k).append(self.client.oas[path[1:]].post)

    def _load_dynamic(self):
        for path in self.client.oas.values():
            if path.post:
                for k, paths in RANKED.items():
                    if path.full_api_endpoint not in paths and getattr(path.post, k).columns:
                        getattr(self, k).append(path.post)

    @property
    def ipv4(self):
        return self._ipv4

    @property
    def ipv6(self):
        return self._ipv6

    @property
    def mac(self):
        return self._mac

    @staticmethod
    def _create_filter(
        columns: List[Union[str, NestedColumn]], arrays: List[str], value: str, regex: bool = False
    ) -> dict:
        oper = "reg" if regex else "eq"
        filters = []
        for col in columns:
            if isinstance(col, NestedColumn):
                filters.append({col.parent: ["any", col.child, oper, value]})
            elif col in arrays:
                filters.append({col: ["any", oper, value]})
            else:
                filters.append({col: [oper, value]})
        return {"or": filters}

    def _search(
        self,
        search_type: Literal["ipv4", "ipv6", "mac"],
        address: str,
        full_scan: bool = False,
        regex: bool = False,
    ) -> Dict[str, Dict[str, Union[str, list]]]:

        results = OrderedDict()

        for path in getattr(self, search_type):
            search_data = getattr(path, search_type)
            if not full_scan and search_data.full_scan is True:
                LOGGER.debug('Finished searching default tables; "--full-scan" not enabled to search all tables.')
                break  # List is ordered and once this is met we can break if not full scan
            filters = self._create_filter(search_data.columns, path.array_columns, address, True if regex else False)
            msg = f'earching "{path.web_menu}": API Endpoint: "{path.full_api_endpoint}"'
            LOGGER.debug(f'S{msg}; Filters `{json.dumps(filters, separators=(",", ":"))}`.')
            results[path.full_api_endpoint] = {
                "data": self.client.fetch_all(path.api_endpoint, filters=filters),
                "path": path.full_api_endpoint,
                "webPath": path.web_endpoint,
                "url": path.filter_url(filters),
                "menu": f'{path.web_menu}: "{path.title or path.summary}"',
            }
            LOGGER.debug(f"Finished s{msg}.")

        return results

    def search(
        self,
        address: str,
        full_scan: bool = False,
    ) -> Union[None, Dict[str, Dict[str, Union[str, list]]]]:

        if isinstance(address, int):
            raise TypeError(f"Input must be a valid string not integer: {str(address)}")
        try:
            return self.search_mac(address, full_scan)
        except ValueError:
            pass
        try:
            return self.search_ip(address, full_scan)
        except ValueError:
            raise SyntaxError(f'Address does not appear to be a IPv4, IPv6, nor MAC Address: "{address}".')

    def search_mac(
        self,
        address: str,
        full_scan: bool = False,
    ) -> Dict[str, Dict[str, Union[str, list]]]:

        if isinstance(address, int):
            raise TypeError(f"Input must be a valid string not integer: {str(address)}")
        LOGGER.info("Verifying Address is a MAC.")
        EUI48(address)
        mac = parse_mac(address)
        LOGGER.debug(f'Searching for MAC Address "{mac}".')
        return self._search("mac", mac, full_scan)

    def search_ip(
        self,
        address: str,
        full_scan: bool = False,
    ) -> Dict[str, Dict[str, Union[str, list]]]:
        LOGGER.info("Verifying Address is an IP.")
        ip = ipaddress.ip_address(address)
        if ip.version == 4:
            LOGGER.debug(f'Searching for IPv4 Address "{str(ip)}".')
            return self._search("ipv4", str(ip), full_scan)
        elif ip.version == 6:
            LOGGER.debug(f'Searching for IPv6 Address "{str(ip)}".')
            return self._search("ipv6", str(ip), full_scan)

    def _search_ip(
        self,
        version: int,
        address: str,
        full_scan: bool = False,
    ) -> Dict[str, Dict[str, Union[str, list]]]:
        ip = ipaddress.ip_address(address)
        if ip.version != version:
            raise ValueError()
        return self._search("ipv" + str(version), str(ip), full_scan)

    def search_ipv4(
        self,
        address: str,
        full_scan: bool = False,
    ) -> Union[None, Dict[str, Dict[str, Union[str, list]]]]:
        return self._search_ip(4, address, full_scan)

    def search_ipv6(
        self,
        address: str,
        full_scan: bool = False,
    ) -> Union[None, Dict[str, Dict[str, Union[str, list]]]]:
        return self._search_ip(6, address, full_scan)

    def search_regex(
        self,
        search_type: Literal["ipv4", "ipv6", "mac"],
        address: str,
        full_scan: bool = False,
    ) -> Dict[str, Dict[str, Union[str, list]]]:
        LOGGER.debug(f'Searching for {search_type.upper()} Address "{address}".')
        return self._search(search_type, address, full_scan, True)
