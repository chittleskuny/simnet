def format_bit_string(bit_string, column=8):
    if len(bit_string) % 8 != 0: # 8 bits per byte
        print('Not a multiple of 8.')
        return None

    line, lines = [], []
    for n in range(len(bit_string) // 8):
        if (n % column == 0) and line:
            number = n - column + 1
            lines.append(('$%d:\t' % number) + ' '.join(line))
            line = []
        byte = bit_string[(n*8):((n + 1)*8)]
        line.append(byte)
    if line:
        number = n - len(line) + 1
        lines.append(('$%d:\t' % number) + ' '.join(line))
    return '\n'.join(lines)
