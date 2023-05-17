import docx
import time

def fsm_search(text, pattern):
    n = len(text) #text to search
    m = len(pattern) #pattern to find

    #DFA, where transitions are created
    dfa = [0] * m #creates array of size m and sets all elements to 0 -> represents the states
    j = 0 #keeps track of current state in machine
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]: #iteratestates until finds a match/reach start state.pattern[j]is current chracter, while pattern[i] is character.
            j = dfa[j - 1] #mismatch occured so update j to previous state
        if pattern[j] == pattern[i]: #match is found
            j += 1 #move to next state
        dfa[i] = j #stores state value at transition index

    #search for pattern
    j = 0 #start of the text
    for i in range(n): #iterate characters
        while j > 0 and text[i] != pattern[j]: #same as in dfa, but text[i] is current char.
            j = dfa[j - 1]
        if text[i] == pattern[j]: #if a match is found, move next
            j += 1
        if j == m: #complete match, returns start index of match
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
