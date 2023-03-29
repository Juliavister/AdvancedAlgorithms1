import docx
import time

def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0
    while i <= n - m:
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
        i += 1
    return -1

doc = docx.Document('/Users/juliavister/Desktop/Raven.docx')
text = '\n'.join([para.text for para in doc.paragraphs])

small_pattern = 'silence'
large_pattern = 'Ah, distinctly I remember it was in the bleak December'

#prints the indexes of where the pattern is found in the file

start_time = time.time()
index_small = brute_force(text, small_pattern)
end_time = time.time()
print(f"Small pattern found at index {index_small}. Time taken: {end_time - start_time} seconds")

start_time = time.time()
index_large = brute_force(text, large_pattern)
end_time = time.time()
print(f"Large pattern found at index {index_large}. Time taken: {end_time - start_time} seconds")

