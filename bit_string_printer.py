def print_bit_string(bit_string, column=8):
    if len(bit_string) % 8 != 0: # 8 bits per byte
        print('Not a multiple of 8.')
        return None

    line = []
    for n in range(len(bit_string) // 8):
        if (n % column == 0) and line:
            print(('%d:\t' % n) + ' '.join(line))
            line = []
        byte = bit_string[(n*8):((n + 1)*8)]
        line.append(byte)

    return 0
