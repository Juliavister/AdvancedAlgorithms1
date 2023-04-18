import timeit
import random
import string

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

def gusfield_z(pattern, text):
    """
       Gusfield's Z algorithm for pattern matching.
       """
    concat = pattern + "$" + text
    z = [0] * len(concat)
    l, r = 0, 0
    for i in range(1, len(concat)):
        if i > r:
            l, r = i, i
            while r < len(concat) and concat[r - l] == concat[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < len(concat) and concat[r - l] == concat[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    matches = []
    for i in range(len(z)):
        if z[i] == len(pattern):
            return i - len(pattern) - 1
    return -1

# specify a pattern of at least 10 characters
pattern = "GTCTCGCGCG"

# specify a long text of at least 100kB
text = "A" * 100000

# test Binary Sunday
binary_sunday_time = timeit.timeit(lambda: binary_sunday(pattern, text), number=10)
print("Binary Sunday time:", binary_sunday_time/10)

# test Gusfield Z
gusfield_z_time = timeit.timeit(lambda: gusfield_z(pattern, text), number=10)
print("Gusfield Z time:", gusfield_z_time/10)


# test with a repeating pattern and text
#pattern = "a" * 1000
#text = "a" * (100 * 1024)

#binary_sunday_time = timeit.timeit(lambda: binary_sunday(pattern, text), number=1)
#print("Binary Sunday time:", binary_sunday_time)


# Time Gusfield Z algorithm
#gusfield_z_time = timeit.timeit(lambda: gusfield_z(pattern, text), number=1)
#print("Gusfield Z time:", gusfield_z_time)
