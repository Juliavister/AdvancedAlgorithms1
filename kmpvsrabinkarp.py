import timeit

def kmp(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    indices = []  # initialize list of indices
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            indices.append(i - j)  # pattern found, add index to list
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices  # return list of indices where pattern is found


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0] = 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


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
