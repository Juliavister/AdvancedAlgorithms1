def rabinKarp(pattern, text):
    pattern_hash = hash(pattern)
    text_hash = hash(text[:len(pattern)])

    results = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i + len(pattern)]:
            results.append(i)

        if i < len(text) - len(pattern):
            text_hash = hash(text[i + 1:i + len(pattern) + 1])

    return results
