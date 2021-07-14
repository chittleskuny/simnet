def format_bit_string(bit_string, line_num=False, indent=0, indent_1st=True, column=8):
    if len(bit_string) % 8 != 0: # 8 bits per byte
        print('Not a multiple of 8.')
        return None

    flag_1st = True
    indent = ' '*indent
    line, lines = [], []
    for n in range(len(bit_string) // 8):
        if (n % column == 0) and line:
            number = n - column + 1
            if flag_1st and not indent_1st:
                if line_num:
                    lines.append(('$%d:\t' % number) + ' '.join(line))
                else:
                    lines.append(' '.join(line))
                flag_1st = not flag_1st
            else:
                if line_num:
                    lines.append(indent + ('$%d:\t' % number) + ' '.join(line))
                else:
                    lines.append(indent + ' '.join(line))
            line = []
        byte = bit_string[(n*8):((n + 1)*8)]
        line.append(byte)
    if line:
        number = n - len(line) + 1
        if flag_1st and not indent_1st:
            if line_num:
                lines.append(('$%d:\t' % number) + ' '.join(line))
            else:
                lines.append(' '.join(line))
        else:
            if line_num:
                lines.append(indent + ('$%d:\t' % number) + ' '.join(line))
            else:
                lines.append(indent + ' '.join(line))
    return '\n'.join(lines)
