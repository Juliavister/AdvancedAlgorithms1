def brute_force(text, pattern, first=True):
    text_len = len(text)
    pattern_len = len(pattern)
    i = 0
    if first:
        j = 0
        while j < pattern_len and pattern[j] == '*':
            j += 1
        if j > 0:
            pattern = pattern[j:]
            pattern_len -= j
    while i <= text_len - pattern_len:
        match_progress = 0
        while match_progress < pattern_len and (
                text[i + match_progress] == pattern[match_progress] or pattern[match_progress] == "?"):
            match_progress += 1
        if match_progress == pattern_len:
            return True
        if pattern[match_progress:match_progress + 1] == '*':
            rec_i = i + match_progress
            while rec_i <= text_len:
                if brute_force(text[rec_i:], pattern[match_progress + 1:], False):
                    return True
                rec_i += 1
        i += 1
    return False
