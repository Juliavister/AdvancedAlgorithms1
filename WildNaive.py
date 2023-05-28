def brute_force(pattern, text):
    pattern_bits = pattern.split('*')
    i = 0
    while i < len(pattern_bits) - 1:
        if pattern_bits[i].endswith('\\'):
            pattern_bits[i] = pattern_bits[i][:-1] + '*'
            pattern_bits[i] += pattern_bits[i + 1]
            del pattern_bits[i + 1]
        else:
            i += 1

    pattern_bits_truth = []
    m = len(pattern)
    n = len(text)
    i = 0

    for pbl in range(len(pattern_bits)):
        pattern_bit_match = False
        pattern_bit = pattern_bits[pbl]
        pbl_len = len(pattern_bit)

        while i <= n - pbl_len:
            j = 0
            while j < pbl_len and (text[i + j] == pattern_bit[j] or pattern_bit[j] == "?"):
                j += 1
            if j == pbl_len:
                pattern_bit_match = True
                break
            i += 1

        pattern_bits_truth.append(pattern_bit_match)
        if not pattern_bit_match:
            break

    if False in pattern_bits_truth:
        return False
    else:
        return True
