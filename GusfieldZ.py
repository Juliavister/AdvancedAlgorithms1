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

import docx
import time

# Open the Word file
doc = docx.Document(r"C:\Users\lenovo\Downloads\Raven.docx")
text = '\n'.join([para.text for para in doc.paragraphs])


#small pattern
pat_small = "silence"
start_time = time.time()
indices_small = gusfield_z(pat_small,text)
elapsed_time_small = time.time() - start_time
print(f"Indices of '{pat_small}' found using Gusfield algorithm: {indices_small}") #it says none
print(f"Elapsed time for small pattern: {elapsed_time_small:.6f} seconds")

#large pattern
pat_large = "Ah, distinctly I remember it was in the bleak December"
start_time = time.time()
indices_large = gusfield_z(pat_large,text)
elapsed_time_large = time.time() - start_time
print(f"Indices of large pattern found using Gusfield algorithm: {indices_large}")
print(f"Elapsed time for large pattern: {elapsed_time_large:.6f} seconds")

