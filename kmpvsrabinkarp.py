import timeit

def kmp(pattern, text):
    m = len(pattern)
    n = len(text)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            # pattern found at position i - m + 1
            return i - m + 1
    # pattern not found
    return -1

def rabin_karp(pattern, text):
    pattern_hash = hash(pattern)
    text_hash = hash(text[:len(pattern)])

    results = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i + len(pattern)]:
            results.append(i)

        if i < len(text) - len(pattern):
            text_hash = hash(text[i + 1:i + len(pattern) + 1])

    return results

# test with a repeating pattern and text
pattern = "ababababab"
text = pattern * (100 * 1024 * 1024 // len(pattern))  # 1MB text

kmp_time = timeit.timeit(lambda: kmp(pattern, text), number=1)
print("KMP:", kmp_time, "seconds")

rk_time = timeit.timeit(lambda: rabin_karp(pattern, text), number=1)
print("Rabin-Karp:", rk_time, "seconds")