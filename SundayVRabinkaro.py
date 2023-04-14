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

def rabin_karp(pattern, text):
    m = len(pattern)
    n = len(text)
    h = pow(2, 8 * (m - 1), 101)
    p = 0
    t = 0
    for i in range(m):
        p = (256 * p + ord(pattern[i])) % 101
        t = (256 * t + ord(text[i])) % 101
    for s in range(n - m + 1):
        if p == t and pattern == text[s:s + m]:
            # pattern found at position s
            return s
        if s < n - m:
            t = (256 * (t - ord(text[s]) * h) + ord(text[s + m])) % 101
            if t < 0:
                t += 101
    # pattern not found
    return -1

# test with a repeating pattern and text
pattern = "a" * 50
text = pattern + "b" * (1024*100 - 50)
# measure execution time using timeit
binary_sunday_time = timeit.timeit(lambda: binary_sunday(pattern, text), number=10)
rabin_karp_time = timeit.timeit(lambda: rabin_karp(pattern, text), number=10)

print("Binary Sunday:", binary_sunday_time, "seconds")
print("Rabin-Karp:", rabin_karp_time, "seconds")