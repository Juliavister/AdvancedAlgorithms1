def brute_force(string, pattern):
    n = len(string)
    m = len(pattern)
    i = 0  # index for string
    j = 0  # index for pattern

    while i < n and j < m:
        if pattern[j] == '\\':  # Check for escaped '*' or '?'
            if j + 1 < m and (pattern[j + 1] == '*' or pattern[j + 1] == '?'):
                if i < n and string[i] == pattern[j + 1]:
                    i += 1
                else:
                    return False
                j += 2
            else:
                if i < n and string[i] == pattern[j + 1]:
                    i += 1
                j += 1
        elif pattern[j] == '?':  # Match any character
            if j + 1 < m and pattern[j + 1] == '\\':
                j += 2
                if i < n:
                    i += 1
            else:
                i += 1
                j += 1
        elif pattern[j] == '*':  # Wildcard * matching
            while i < n and (j + 1 >= m or string[i] != pattern[j + 1]):
                i += 1
            j += 1
        else:  # Normal character matching
            if i < n and string[i] == pattern[j]:
                i += 1
                j += 1
            else:
                return False

    if j == m:  # If pattern is fully matched
        return True

    return False
