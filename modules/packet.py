from .formatter import format_bit_string
from .ip import *

version_numbers = [
    None,    #0
    None,    #1
    None,    #2
    None,    #3
    'IP',    #4
    'ST',    #5
    'IPv6',  #6
    'TP/IX', #7
    'PIP',   #8
    'TUBA',  #9
]

packet_str_tmp = '''
    version               : %s
    internet header length: %s
    type of service       : %s
    total length          : %s
    identification        : %s
    flags                 : %s
    fragment offset       : %s
    time to live          : %s
    protocol              : %s
    header checksum       : %s
    src address           : %s
    dest address          : %s
    options               : %s
    data                  : %s
'''

class Packet(object):
    def __init__(self,
            version=None,
            id=None,
            dont_fragment=None,
            more_fragment=None,
            fragment_offset=None,
            time_to_live=None,
            protocol=None,
            src_address=None,
            dest_address=None,
            options=None,
            data=None,
            bit_string=None,
        ):
        if version is not None \
                and id is not None \
                and dont_fragment is not None \
                and more_fragment is not None \
                and fragment_offset is not None \
                and time_to_live is not None \
                and protocol is not None \
                and src_address is not None \
                and dest_address is not None \
                and data is not None:
            self.version = version_numbers.index(version)

            if options is None:
                self.options = ''
                self.padding = ''
                self.internet_header_length = 5
            else:
                self.options = options
                self.padding = ('00000000'*4)[len(options):]
                self.internet_header_length = 6

            self.type_of_service = '00000000'

            self.identification = id

            self.flags = '0' + str(dont_fragment) + str(more_fragment)
            self.fragment_offset = fragment_offset

            self.time_to_live = time_to_live
            self.protocol = protocol

            self.header_checksum = '00000000'*2

            self.src_address = Ip(src_address)
            self.dest_address = Ip(dest_address)
            self.data = data
            self.total_length = self.internet_header_length + len(data)

            self.bit_string = self.bit_string_concat()

        if bit_string is not None:
            self.bit_string = bit_string
            self.bit_string_parse()

    def bit_string_concat(self):
        if self.version == 4:
            bit_string_list = [

                # 4*8*1
                bin(self.version)[2:].rjust(4, '0'),
                bin(self.internet_header_length)[2:].rjust(4, '0'),
                self.type_of_service,
                bin(self.total_length)[2:].rjust(16, '0'),

                # 4*8*2
                bin(self.identification)[2:].rjust(16, '0'),
                self.flags,
                bin(self.fragment_offset)[2:].rjust(13, '0'),

                # 4*8*3
                self.time_to_live,
                self.protocol,
                self.header_checksum,

                # 4*8*4
                self.src_address.address_bin,

                # 4*8*5
                self.dest_address.address_bin,

                # 4*8*5 or 4*8*6
                self.options, self.padding,

                # others
                self.data

            ]
            return ''.join(bit_string_list)

        if self.version == 6:
            return None

        return None

    def bit_string_parse(self):
        self.version = int(self.bit_string[:4], 2)
        
        if self.version == 4:
            self.internet_header_length = int(self.bit_string[4:8], 2)
            self.type_of_service = self.bit_string[8:16]
            self.total_length = int(self.bit_string[16:32], 2)
            self.identification = int(self.bit_string[32:48], 2)
            self.flags = self.bit_string[48:51]
            self.fragment_offset = int(self.bit_string[51:64], 2)
            self.time_to_live = self.bit_string[64:72]
            self.protocol = self.bit_string[72:80]
            self.header_checksum = self.bit_string[80:96]
            self.src_address = Ip(self.bit_string[96:128])
            self.dest_address = Ip(self.bit_string[128:160])

            if self.internet_header_length == 5:
                self.options = ''
                self.padding = ''
                self.data = self.bit_string[160:]

            if self.internet_header_length == 6:
                self.options = self.bit_string[160:192]
                self.padding = ''
                self.data = self.bit_string[192:]

        if self.version == 6:
            pass

    def __str__(self):
        return packet_str_tmp % (
            self.version,
            self.internet_header_length,
            self.type_of_service,
            self.total_length,
            self.identification,
            self.flags,
            self.fragment_offset,
            self.time_to_live,
            self.protocol,
            format_bit_string(self.header_checksum),
            self.src_address.address,
            self.dest_address.address,
            self.options,
            format_bit_string(self.data),
        )
