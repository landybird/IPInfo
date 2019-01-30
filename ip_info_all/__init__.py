from collections import namedtuple
import netifaces as ni
class IPInfo(object):
    """
    Get IPV4 or IPV6 IP info
    """

    def __init__(self):
        self.interface_list = ni.interfaces()
        self.ip_info_list = [(item, ni.ifaddresses(item)) for item in self.interface_list]
        self.info_tuple = namedtuple("IPInfo", "addr netmask broadcast")

    @property
    def all_ipv4_ip_info_dict(self):
        info_dict = dict()
        for item, info in  self.ip_info_list:
            ipv4_info = info.get(2, None)
            if ipv4_info:
                info_dict[item] = self.info_tuple(addr=ipv4_info[0].get("addr", None), netmask=ipv4_info[0].get("addr", None),broadcast=ipv4_info[0].get("addr", None))
        return info_dict

    def get_ipv4_ip_by_encap(self, encap_name, param="addr"):
        info_dict = self.all_ipv4_ip_info_dict
        info_tuple = info_dict.get(encap_name, None)
        if info_tuple:
            if param.upper() == "all".upper():
                return info_tuple.addr, info_tuple.netmask, info_tuple.broadcast
            elif param.upper() == "netmask".upper():
                return info_tuple.netmask
            elif param.upper() == "broadcast".upper():
                return info_tuple.netmask
            else:
                return info_tuple.addr


    @property
    def all_ipv6_ip_info_dict(self):
        info_dict = dict()
        for item, info in  self.ip_info_list:
            ipv6_info = info.get(23, None)
            if ipv6_info:
                info_dict[item] = self.info_tuple(addr=ipv6_info[0].get("addr", None), netmask=ipv6_info[0].get("addr", None),broadcast=ipv6_info[0].get("addr", None))
        return info_dict

    def get_ipv6_ip_by_encap(self, encap_name, param="addr"):
        info_dict = self.all_ipv6_ip_info_dict
        info_tuple = info_dict.get(encap_name, None)
        if info_tuple:
            if param.upper() == "all".upper():
                return info_tuple.addr, info_tuple.netmask, info_tuple.broadcast
            elif param.upper() == "netmask".upper():
                return info_tuple.netmask
            elif param.upper() == "broadcast".upper():
                return info_tuple.netmask
            else:
                return info_tuple.addr

if __name__ == '__main__':
    print(IPInfo().all_ipv4_ip_info_dict)
