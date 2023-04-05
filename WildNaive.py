import re


def brute_force(text, pattern):
    pattern_regex = pattern.replace('*', '\S*').replace('?', r'\S')
    pattern_regex = r'{}\b'.format(pattern_regex)
    n = len(text)
    m = len(pattern)
    i = 0
    matches = []
    while i <= n - m:
        j = 0
        while j < m and (text[i + j] == pattern[j] or pattern[j] == "?"):
            j += 1
        if j == m:
            matches.append(i)
        i += 1
    regex_matches = [m.start() for m in re.finditer(pattern_regex, text)]
    return sorted(list(set(matches + regex_matches)))
