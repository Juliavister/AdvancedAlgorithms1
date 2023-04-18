import timeit

def binary_sunday(pattern, text):
    matches = []
    m = len(pattern)
    n = len(text)
    skip_table = {}
    for i in range(m):
        skip_table[pattern[i]] = m - i
    i = 0
    while i <= n - m:
        # check if the current character is a potential match
        if text[i] in skip_table:
            j = 0
            while j < m and (text[i + j] == pattern[j]):
                j += 1
            if j == m:
                matches.append(i)
            i += skip_table[text[i]]
        else:
            i += m + 1
    return matches

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
pattern =  "ababababababababababab"


text = pattern * 100000

# measure execution time using timeit
binary_sunday_time = timeit.timeit(lambda: binary_sunday(pattern, text), number=10)
rabin_karp_time = timeit.timeit(lambda: rabin_karp(pattern, text), number=10)

print("Binary Sunday:", binary_sunday_time, "seconds")
print("Rabin-Karp:", rabin_karp_time, "seconds")
