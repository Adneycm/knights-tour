import numpy as np

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Get the keys in sorted order
sorted_keys = list(sorted_dict.keys())

print(sorted_keys)

