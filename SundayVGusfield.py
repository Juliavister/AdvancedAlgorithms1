import timeit

def binary_sunday(pattern, text):
    m = len(pattern)
    n = len(text)
    skip = [m] * 256
    for i in range(m):
        skip[ord(pattern[i])] = m - i - 1
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            # pattern found at position i
            return i
        i += skip[ord(text[i + m])] if i + m < n else 1
    # pattern not found
    return -1

def gusfield_z(pattern, text):
    m = len(pattern)
    n = len(text)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            j = 0
            while i + j < n and text[i + j] == text[j]:
                j += 1
            if j > 0:
                z[i] = j
                l, r = i, i + j - 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                j = r - i + 1
                while r + j < n and text[r + j] == text[r - i + 1 + j]:
                    j += 1
                z[i] = r - i + 1 + j
                l, r = i, r + j - 1
        if z[i] == m:
            # pattern found at position i - m - 1
            return i - m - 1
    # pattern not found
    return -1

# test with a repeating pattern and text
pattern = "ababababab"
text = pattern * ( 1024 * 1024 // len(pattern))  # 1MB text
binary_sunday_time = timeit.timeit(lambda: binary_sunday(pattern, text), number=100)
print("Binary Sunday time:", binary_sunday_time)


# Time Gusfield Z algorithm
gusfield_z_time = timeit.timeit(lambda: gusfield_z(pattern, text), number=100)
print("Gusfield Z time:", gusfield_z_time)
