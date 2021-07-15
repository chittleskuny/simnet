from .formatter import format_bit_string

mac_str_tmp = '''
    address bin: %s
    address hex: %s
    cast       : %s
    scope      : %s
    vendor     : %s
    product    : %s
'''

class Mac(object):
    def __init__(self, address):
        if len(address) == 48:
            self.address_bin = address
            self.address_hex = self.from_bin_to_hex()       
        if len(address) == 17:
            self.address_hex = address
            self.address_bin = self.from_hex_to_bin()

    def from_bin_to_hex(self):
        address_hex_list = []
        for i in range(0, 48, 8):
            i_bin = self.address_bin[(i):(i + 8)]
            i_hex = hex(int(i_bin, 2))[2:]
            address_hex_list.append(i_hex)
        return ':'.join(address_hex_list)
        
    def from_hex_to_bin(self):
        address_bin_list = []
        address_hex_list = self.address_hex.split(':')
        for i in address_hex_list:
            i_bin = bin(int(i, 16))[2:]
            i_bin_rjust = i_bin.rjust(8, '0')
            address_bin_list.append(i_bin_rjust)
        return ''.join(address_bin_list)

    def __str__(self):
        return mac_str_tmp % (
            format_bit_string(self.address_bin, indent_1st=False),
            self.address_hex,
            self.address_bin[0],
            self.address_bin[1],
            self.address_bin[2:24],
            self.address_bin[24:48],
        )
