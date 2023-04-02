import re  # module for handling regular expressions


# TODO: make regular expressions handling manually

def wildSundaySearch(pattern, text):
    pattern_regex = pattern.replace('*', '\S*').replace('?', r'\S')
    pattern_regex = r'{}\b'.format(pattern_regex)
    # those two lines above and the last two can handle everything and i have no idea for now how to handle regular
    # expressions manually so i leave it as is for now, both codes are used (mine and lib) even tho mine is kind of
    # redundant, explanation how Sunday's algorithm works will be in at the bottom, for some lines i'll add comments too
    matches = []  # list of all matches
    m = len(pattern)
    n = len(text)
    skip_table = {}  # see skip table explanation at the bottom
    for i in range(m):
        skip_table[pattern[i]] = m - i
    i = 0
    while i <= n - m:  # checks if pattern isn't already moved past checked text
        j = 0
        # j counts matches until there aren't as many as pattern is long, match is same character or ?
        while j < m and (text[i + j] == pattern[j] or pattern[j] == "?"):
            j += 1
        if j == m:  # if there are as many matching characters as pattern's length then add position i as match
            matches.append(i)
        if i + m >= n:  # checks if text isn't exceeded already, if so then breaks
            break
        if text[i + m] in skip_table:  # see skip table explanation at the bottom
            i += skip_table[text[i + m]]
        else:
            i += m + 1
    regex_matches = [m.start() for m in re.finditer(pattern_regex, text)]  # m.start() gets starting positions of stuff
    # found by re.finditer() and saves it in regex_matches
    return sorted(list(set(matches + regex_matches)))  # mixes results from re and my code and returns them

# shift_table and Sunday's algorithm overall:
# code at first mention of shift_table gives each letter in pattern a value, that value will be used later to determine
# how far do we need to move our pattern in relation to checked text above. I.E. ABC will have following results:
# A = 3, B = 2, C = 1.

# the best way to explain Sunday's algorithm will be with an example
# Let's say pattern is ABC and our text is FABCDE, in skip_table = {A=3,B=2,C=1}
# First we align both text and pattern to the left:
# FABCDE            and now we check matches from right to left, F and A don't match already, so now we look
# ABC               at our skip_table checking if we have there character that's the first one to the right
#                   after our pattern stopped aligning with text, in this case it's C, it exists in
# skip table, and it has a value of 1, so we move our pattern to the right by 1, it now should look like this:
# FABCDE            so now we check from left to right and A=A, B=B, C=C, great success! We have a match but
#  ABC              we need to look further if there are more matches, we look at character where strings
#                   stop aligning, and we see D, D is not in skip_table, so we use formula that in this code
# is in else statement just below, m+1 where m is of course the length of our pattern, in this case 3+1=4
# we move our pattern by 4 which would give us a placement like this:
# FABCDE            at this point our algorithm stops because i which you can think of as those empty spaces
#      ABC          on the left of pattern is obviously larger than text's length - pattern's length which
# breaks from our main while loop that goes only while <= n-m
