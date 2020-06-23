class OSIRM(object):
    def __init__(self):
        pass

    # desc: 7->6->5->4->3->2->1

    def desc_7_application_layer(self, data):
        return '|'.join(['head_7', data])

    def desc_6_presentation_layer(self, data):
        return '|'.join(['head_6', data])

    def desc_5_session_layer(self, data):
        return '|'.join(['head_5', data])

    def desc_4_transport_layer(self, data):
        return '|'.join(['head_4', data])

    def desc_3_network_layer(self, data):
        return '|'.join(['head_3', data])

    def desc_2_data_link_layer(self, data):
        return '|'.join(['head_2', data])

    def desc_1_physical_layer(self, data):
        return '|'.join(['head_1', data])

    # asc:  1->2->3->4->5->6->7

    def asc_1_physical_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_2_data_link_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_3_network_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_4_transport_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_5_session_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_6_presentation_layer(self, head_body):
        return head_body.split('|', 1)[1]

    def asc_7_application_layer(self, head_body):
        return head_body.split('|', 1)[1]


if __name__ == '__main__':
    osirm = OSIRM()

    desc_input_7 = input('message: ')

    print(desc_input_7)
    desc_output_7 = osirm.desc_7_application_layer(desc_input_7)
    print(desc_output_7)
    desc_output_6 = osirm.desc_6_presentation_layer(desc_output_7)
    print(desc_output_6)
    desc_output_5 = osirm.desc_5_session_layer(desc_output_6)
    print(desc_output_5)
    desc_output_4 = osirm.desc_4_transport_layer(desc_output_5)
    print(desc_output_4)
    desc_output_3 = osirm.desc_3_network_layer(desc_output_4)
    print(desc_output_3)
    desc_output_2 = osirm.desc_2_data_link_layer(desc_output_3)
    print(desc_output_2)
    desc_output_1 = osirm.desc_1_physical_layer(desc_output_2)
    print(desc_output_1)

    print('------')
    asc_input_1 = desc_output_1 # by electricity
    print('------')

    print(asc_input_1)
    asc_output_1 = osirm.asc_1_physical_layer(asc_input_1)
    print(asc_output_1)
    asc_output_2 = osirm.asc_2_data_link_layer(asc_output_1)
    print(asc_output_2)
    asc_output_3 = osirm.asc_3_network_layer(asc_output_2)
    print(asc_output_3)
    asc_output_4 = osirm.asc_4_transport_layer(asc_output_3)
    print(asc_output_4)
    asc_output_5 = osirm.asc_5_session_layer(asc_output_4)
    print(asc_output_5)
    asc_output_6 = osirm.asc_6_presentation_layer(asc_output_5)
    print(asc_output_6)
    asc_output_7 = osirm.asc_7_application_layer(asc_output_6)
    print(asc_output_7)
