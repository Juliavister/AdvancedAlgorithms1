import docx2txt
import time

def fsm_search(text, pattern):
    n = len(text)
    m = len(pattern)

    #making the DFA
    dfa = [0] * m
    dfa[0] = -1
    j = -1
    for i in range(1, m):
        while j >= 0 and pattern[j + 1] != pattern[i]:
            j = dfa[j]
        if pattern[j + 1] == pattern[i]:
            j += 1
        dfa[i] = j

    #searching for the pattern
    j = -1
    for i in range(n):
        while j >= 0 and pattern[j + 1] != text[i]:
            j = dfa[j]
        if pattern[j + 1] == text[i]:
            j += 1
        if j == m - 1:
            return i - m + 1

    return -1

chapter = docx2txt.process('/Users/juliavister/Desktop/Raven.docx')
small_pattern = 'silence'
large_pattern = 'Ah, distinctly I remember it was in the bleak December'

start_time = time.time()
result_small = fsm_search(chapter, small_pattern)
end_time = time.time()
print(f'Small pattern found at index {result_small} in {end_time - start_time} seconds')

start_time = time.time()
result_large = fsm_search(chapter, large_pattern)
end_time = time.time()
print(f'Large pattern found at index {result_large} in {end_time - start_time} seconds')

