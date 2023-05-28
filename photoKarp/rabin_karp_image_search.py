def r_hash(s, base=256, prime=101):
    if isinstance(s[0][0], str):
        # Use ASCII codes for characters
        h = 0
        for row in s:
            for c in row:
                h = (h * base + ord(c)) & (prime - 1)
                # Remove contribution of the first character in the previous window
                if len(row) > 1:
                    h = (h - (ord(row[0]) * pow(base, len(row) - 1, prime))) & (prime - 1)
    else:
        # Use polynomial hash for numbers
        h = 0
        for row in s:
            for c in row:
                h = (h * base + c) & (prime - 1)
                # Remove contribution of the first number in the previous window
                if len(row) > 1:
                    h = (h - (row[0] * pow(base, len(row) - 1, prime))) & (prime - 1)
    return h


def rabin_karp_image_search(image, pattern):
    m, n = image.shape[:2]
    k, l = pattern.shape[:2]
    pattern_hash = r_hash(pattern)
    for i in range(m - k + 1):
        # Calculate the hash value for the first window in each row
        window_hash = r_hash(image[i:i + k, :l])
        if window_hash == pattern_hash and (image[i:i + k, :l] == pattern).all():
            return True
        for j in range(1, n - l + 1):
            # Slide the window horizontally and update the hash value
            window_hash = r_hash(image[i:i + k, j:j + l])
            if window_hash == pattern_hash and (image[i:i + k, j:j + l] == pattern).all():
                return True
    return False
