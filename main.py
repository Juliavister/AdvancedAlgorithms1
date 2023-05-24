import timeit
import matplotlib.pyplot as plt
import numpy as np
from Algorithms import Sunday, KMP, Naive, GusfieldZ, FSM, RabinKarpNew

with open('karamazov.txt', encoding='utf8') as f:
    poem = f.read().replace('\n', ' ')
#
# patternWild = "I ?as a\*"
pattern = "Abrakadabra hokus pokus"

# print("Sunday with wildcards: ")
# print(SundayWildcards.wildSundaySearch(patternWild, poem))
# print("Naive/Bruteforce: ")
# print(WildNaive.brute_force(patternWild, poem))

results = []
x_axis = []

prime = 101
#lines = 5000
#while lines < 37628:
for lines in range(5000*100, len(poem),5000*100):
    data = poem[:lines]

    SundayTime = timeit.timeit(lambda: Sunday.sundaySearch(pattern, data), number=1) #*1000
    FSMTime = timeit.timeit(lambda: FSM.fsm_search(data, pattern), number=1) #*1000
    GusfieldZTime = timeit.timeit(lambda: GusfieldZ.gusfield_z(pattern, data), number=1) #*1000
    NaiveTime = timeit.timeit(lambda: Naive.brute_force(data, pattern), number=1) #*1000
    KMPTime = timeit.timeit(lambda: KMP.KMPSearch(data, pattern), number=1) #*1000
    RabinKarpNewTime = timeit.timeit(lambda: RabinKarpNew.search(pattern, data, prime), number=1) #*1000

    #print(len(data))
    results.append([SundayTime, FSMTime, GusfieldZTime, NaiveTime, KMPTime, RabinKarpNewTime])
    x_axis.append(len(data)) #(lines)


names = {0: 'Sunday', 1: 'FSM', 2: 'Gusfield-Z', 3: 'Naive', 4: 'KMP', 5: 'Rabin Karp'}
for itera, sublist in enumerate(results):
    print(f"{(1+itera)*5000} lines")
    for ite, item in enumerate(sublist):
        print(names[ite])
        print(item)
    print('\n')

results = np.transpose(results)
plt.plot(x_axis, np.transpose(results))
plt.xlabel("Text Length")
plt.ylabel("Time (seconds)")
plt.legend([names[i] for i in range(len(names))])
plt.show()

