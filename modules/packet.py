from .formatter import format_bit_string

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

            self.src_address = src_address
            self.dest_address = dest_address
            self.data = data
            self.total_length = self.internet_header_length + len(data)

        if bit_string is not None:
            self.bit_string = bit_string

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
            format_bit_string(self.src_address),
            format_bit_string(self.dest_address),
            self.options,
            format_bit_string(self.data),
        )
