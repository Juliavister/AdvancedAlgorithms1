#Rabin Karp algorithm matches the hash value of the pattern with the hash value of the current substring of text,
#and if the hash values match then only it starts matching individual characters

nc = 256 #number of characters in ASCII table
prime = 101 #used for calculations

def search(pattern, text, prime):
    M = len(pattern)
    N = len(text)
    i = 0 #i and j -> counters
    j = 0
    p = 0 #pattern hash value
    t = 0 #text hash value
    h = 1 #hash value

    for i in range(M-1):
        h = (h*nc) % prime #calculate the value of hash

    for i in range(M):
        # ord is a way to convert character to integer, so get numeric value of pattern and text chars
        p = (nc*p + ord(pattern[i])) % prime #calculate pattern hash value
        t = (nc*t + ord(text[i])) % prime #calculate text hash value

    occurrences = []
    #iterate the text to find the pattern by going through hash values of the pattern (it compares it to current hash window, t)
    for i in range(N-M+1):
        if p == t: #if hash values match, compares character by character to make sure match is correct
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1
            else:
                occurrences.append(i)
            if j == M:
                print("Pattern found: " + str(i))

#we need to recalculate the hash(update it) for next window of the text.
        if i < N-M:
            t = (nc * (t-ord(text[i])* h) + ord(text[i+M])) % prime
            #(t-ord(text[i])* h), here we substract what a previous character on the hash value has done,
            # so that we remove the first character and add a new on, so can now move to next window of hash. (so that we dont repeat that one, i think..)
            if t < 0:
                t = t+prime #make sure hash value is within our range

    return occurrences