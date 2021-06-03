from .formatter import format_bit_string

bin_hex = {
    '0000':'0', '0001':'1', '0010':'2', '0011':'3',
    '0100':'4', '0101':'5', '0110':'6', '0111':'7',
    '1000':'8', '1001':'9', '1010':'a', '1011':'b',
    '1100':'c', '1101':'d', '1110':'e', '1111':'f',
}
hex_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
    'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111',
}

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
            left = bin_hex[self.address_bin[(i):(i + 4)]]
            right = bin_hex[self.address_bin[(i + 4):(i + 8)]]
            address_hex_list.append(left + right)
        return ':'.join(address_hex_list)
        
    def from_hex_to_bin(self):
        address_bin_list = []
        address_hex_list = self.address_hex.split(':')
        for i in address_hex_list:
            address_bin_list.append(hex_bin[i[0]])
            address_bin_list.append(hex_bin[i[1]])
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
