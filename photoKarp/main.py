import numpy as np
from rabin_karp_image_search import rabin_karp_image_search

image = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 1, 2, 3],
                  [4, 5, 6, 7]])
pattern = np.array([[2, 3],
                    [6, 7]])
location = rabin_karp_image_search(image, pattern)
print(location)


image2 = np.array([[1,'b','c','d'],
                   ['a',1,'e','f'],
                   ['z','z','z','z']])
pattern2 = np.array([['a','1'],
                     ['h','z']])
location2 = rabin_karp_image_search(image2,pattern2)
print(location2)