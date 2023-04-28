def wildSundaySearch(pattern, text):
    m = len(pattern)
    n = len(text)
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
    skip_table = {}
    for i in range(m):
        skip_table[pattern[i]] = m - i
    i = 0
    for pbl in range(len(pattern_bits)):
        pattern_bit_match = False
        while i <= n - m:
            j = 0
            while j < len(pattern_bits[pbl]) and (text[i + j] == pattern_bits[pbl][j] or pattern_bits[pbl][j] == "?"):
                j += 1
            if j == len(pattern_bits[pbl]):
                pattern_bit_match = True
                break
            if i + len(pattern_bits[pbl]) >= n:
                break
            if text[i + len(pattern_bits[pbl])] in skip_table:
                i += skip_table[text[i + len(pattern_bits[pbl])]]
            else:
                i += len(pattern_bits[pbl]) + 1
        pattern_bits_truth.append(pattern_bit_match)
        if not pattern_bit_match:
            break
    if False in pattern_bits_truth:
        return False
    else:
        return True
