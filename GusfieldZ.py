def gusfield_z(pattern, text):
    """
    Gusfield's Z algorithm for pattern matching.
    """
    concat = pattern + "$" + text # Concatenating them helps simplify the algorithm's logic and allows us to find matches efficiently using the Z-array.
    z = [0] * len(concat)
    l, r = 0, 0
    for i in range(1, len(concat)): # iterate through concat start for index 1 bc index 0 is always 0
        if i > r: # if true, means we dont have info abt the lcp(longest common prefix) beyond this point so we need to compare the pattern with the suffix to fing lcp
            l, r = i, i #set a new Z-box with the values
            while r < len(concat) and concat[r - l] == concat[r]: #until a mismatch is found or concat reaches the end
                r += 1 #expand the Z-box 
            z[i] = r - l #the Z value at the current position is set as the length of the matching prefix, which is r - l 
            r -= 1
        else: # we have info about available from previous calculations
            k = i - l #relative position within the z box
            if z[k] < r - i + 1: # if the k value is less than the remaining length
                z[i] = z[k] # copy the value
            else: #otherwise,
                l = i
                while r < len(concat) and concat[r - l] == concat[r]: # comparing characters from the rightmost position (r) until a mismatch is found or the concat reaches the end
                    r += 1 # expand the Z-box
                z[i] = r - l # The Z-value at the current position is set as the length of the new matching prefix, which is (r - l).
                r -= 1
    matches = [] # After calculating the Z-values for all positions, we iterate through the Z-array to find matches.
    for i in range(len(z)):  # If a Z-value is equal to the length of the pattern, it means we have found a match.
        if z[i] == len(pattern):
            return i - len(pattern) - 1
    return -1 # no match is found

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

