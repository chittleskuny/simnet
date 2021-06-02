from .formatter import format_bit_string
from .mac import *

frame_str_tmp = '''
    dest mac: %s
    src mac : %s
    data    : \n%s
'''

class Frame(object):
    def __init__(self, dest_mac=None, src_mac=None, data=None, bit_string=None):
        if dest_mac is not None and src_mac is not None and data is not None:
            self.preamble = '10101010'*7 + '10101011'*1
            self.dest_mac = Mac(dest_mac)
            print(self.dest_mac.address_bin)
            self.src_mac = Mac(src_mac)
            self.data = data
            self.frame_check_sequence = '????????'*4
            self.bit_string = self.preamble + self.dest_mac.address_bin + self.src_mac.address_bin + self.data + self.frame_check_sequence

        if bit_string is not None:
            self.bit_string = bit_string
            preamble_start, preamble_end = 0, 8*8 # ('10101010'*7 + '10101011'*1) or ('10'*31 + '11'*1)
            self.preamble = bit_string[preamble_start:preamble_end]
            dest_mac_start, dest_mac_end = preamble_end, (preamble_end + 8*6) # '????????'*6
            self.dest_mac = Mac(bit_string[dest_mac_start:dest_mac_end])
            src_mac_start, src_mac_end = dest_mac_end, (dest_mac_end + 8*6) # '????????'*6
            self.src_mac = Mac(bit_string[src_mac_start:src_mac_end])
            frame_check_sequence_start, frame_check_sequence_end = (0 - 8*4), None #'????????'*4
            self.frame_check_sequence = bit_string[frame_check_sequence_start:]
            data_start, data_end = src_mac_end, frame_check_sequence_start # '????????'*(46~1500)
            self.data = bit_string[data_start:data_end]

    def check(self):
        return True

    def __str__(self):
        return frame_str_tmp % (self.dest_mac.address_hex, self.src_mac.address_hex, format_bit_string(self.data))
