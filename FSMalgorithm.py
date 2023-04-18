import docx
import time

def fsm_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # DFA
    dfa = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = dfa[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        dfa[i] = j

    # search for pattern
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = dfa[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def find_pattern_in_book(book_path, small_pattern, large_pattern):
    doc = docx.Document('/Users/juliavister/Desktop/Raven.docx')
    text = '\n'.join([para.text for para in doc.paragraphs])

    start_time = time.time()
    small_result = fsm_search(text, small_pattern)
    end_time = time.time()
    if small_result != -1:
        print(f"Small pattern found at index {small_result}  in {end_time - start_time} seconds")
    else:
        print("Small pattern not found")

    start_time = time.time()
    large_result = fsm_search(text, large_pattern)
    end_time = time.time()
    if large_result != -1:
        print(f"Large pattern found at index {large_result}  in {end_time - start_time} seconds")
    else:
        print("Large pattern not found")


book_path = "/Users/juliavister/Desktop/Raven.docx"
small_pattern = "silence"
large_pattern = "Ah, distinctly I remember it was in the bleak December"
find_pattern_in_book(book_path, small_pattern, large_pattern)