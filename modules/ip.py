from .formatter import format_bit_string

ipv4_str_tmp = '''
    ip version : %s
    address bin: %s
    address dec: %s
'''
ipv6_str_tmp = '''
    ip version : %s
    address bin: %s
    address hex: %s
'''

class Ip(object):
    def __init__(self, address):
        if address.find('.') != -1:
            self.version = 4
            self.address_dec = address
            self.address_bin = self.from_dec_to_bin()
            self.address_hex = None
        if address.find(':') != -1:
            self.version = 6
            self.address_hex = address
            self.address_bin = self.from_hex_to_bin()
            self.address_dec = None

    def from_bin_to_dec(self):
        pass

    def from_bin_to_hex(self):
        pass

    def from_dec_to_bin(self):
        address_bin_list = []
        address_dec_list = self.address_dec.split('.')
        for i in address_dec_list:
            i_bin = bin(int(i, 10))[2:]
            i_bin_rjust = i_bin.rjust(8, '0')
            address_bin_list.append(i_bin_rjust)
        return ''.join(address_bin_list)

    def from_hex_to_bin(self):
        address_bin_list = []
        address_hex_list = self.address_hex.split(':')
        for i in address_hex_list:
            i_bin = bin(int(i, 16))[2:]
            i_bin_rjust = i_bin.rjust(16, '0')
            address_bin_list.append(i_bin_rjust)
        return ''.join(address_bin_list)

    def __str__(self):
        if self.version == 4:
            return ipv4_str_tmp % (
                self.version,
                format_bit_string(self.address_bin, line_num=False),
                self.address_dec,
            )
        elif self.version == 6:
            return ipv6_str_tmp % (
                self.version,
                format_bit_string(self.address_bin, line_num=True, indent=17, indent_1st=False),
                self.address_hex,
            )
        else:
            return str(None)
