from modules.formatter import *
from modules.frame import *
from modules.packet import *

class TCPIP(object):
    def __init__(self):
        pass

    # desc: 4->3->2->1

    def desc_4_application_layer(self, input):
        output = input
        return output

    def desc_3_transport_layer(self, input):
        output = input
        return output

    def desc_2_internet_layer(self, input):
        data = '00000000'
        packet = Packet(
            version=4,
            id=1,
            dont_fragment=0,
            more_fragment=0,
            fragment_offset=1,
            time_to_live='00000000',
            protocol='00000000',
            src_address='192.168.1.1',
            dest_address='192.168.1.2',
            data=data,
        )
        output = packet.bit_string
        return output

    def desc_1_network_access_layer(self, input):
        frame = Frame(
            dest_mac='00:00:00:00:00:00',
            src_mac='00:00:00:00:00:00',
            data=input
        )
        output = frame.bit_string
        return output

    # asc:  1->2->3->4

    def asc_1_network_access_layer(self, input):
        frame = Frame(bit_string=input)
        output = frame.data
        return output

    def asc_2_internet_layer(self, input):
        packet = Packet(bit_string=input)
        output = packet.data
        return output

    def asc_3_transport_layer(self, input):
        output = input
        return output

    def asc_4_application_layer(self, input):
        output = input
        return output


if __name__ == '__main__':
    tcpip = TCPIP()

    desc_input_4 = input('message: ')

    desc_output_4 = tcpip.desc_4_application_layer(desc_input_4)
    print(desc_output_4)
    desc_output_3 = tcpip.desc_3_transport_layer(desc_output_4)
    print(desc_output_3)
    desc_output_2 = tcpip.desc_2_internet_layer(desc_output_3)
    print(desc_output_2)
    desc_output_1 = tcpip.desc_1_network_access_layer(desc_output_2)
    print(desc_output_1)

    print('------')
    asc_input_1 = desc_output_1 # by electricity
    print('------')

    print(asc_input_1)
    asc_output_1 = tcpip.asc_1_network_access_layer(asc_input_1)
    print(asc_output_1)
    asc_output_2 = tcpip.asc_2_internet_layer(asc_output_1)
    print(asc_output_2)
    asc_output_3 = tcpip.asc_3_transport_layer(asc_output_2)
    print(asc_output_3)
    asc_output_4 = tcpip.asc_4_application_layer(asc_output_3)
    print(asc_output_4)
