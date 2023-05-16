def rolling_hash(s, base=256, prime=101):
    if isinstance(s[0, 0], str):
        # Use ASCII codes for characters
        h = 0
        for row in s:
            for c in row:
                h = (h * base + ord(c)) % prime
    else:
        # Use polynomial hash for numbers
        h = 0
        for row in s:
            for c in row:
                h = (h * base + c) % prime
    return h


def rabin_karp_image_search(image, pattern):
    m, n = image.shape[:2]
    k, l = pattern.shape[:2]
    pattern_hash = rolling_hash(pattern)
    for i in range(m - k + 1):
        for j in range(n - l + 1):
            window = image[i:i + k, j:j + l]
            window_hash = rolling_hash(window)
            if window_hash == pattern_hash and (window == pattern).all():
                return True
    return False
