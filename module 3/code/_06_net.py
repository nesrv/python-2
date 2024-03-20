

class IpAddress:

    def __init__(self, ip=''):
        self.ip = list(map(int, ip.split('.')))

    def show_bin_ip(self):
        ip_address = (f'{ip:b}'.zfill(8) for ip in self.ip)
        print(*ip_address)

    def __mul__(self, other):
        res = (ip1 & ip2 for ip1, ip2 in zip(self.ip, other.ip))
        return tuple(res)

    def __repr__(self):
        return str(*self.ip)


ip_address = IpAddress('142.9.227.146')
ip_address.show_bin_ip()  # 10001110 00001001 11100011 10010010
subnet_mask = IpAddress('255.255.192.0')
ip_net = ip_address * subnet_mask
print(ip_net) #(142, 9, 192, 0)
