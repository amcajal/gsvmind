initial_list = ['a', 'b', 'c', 'first_end', 'val1', 'val2', 'val3', 'second_end', 'e', 'f', 'g']
subset = [initial_list[x] for x in range(2, 4)] # This is one way to get a subset
print subset
subset2 = initial_list[2:3] # This is another way to get a subset
print subset
print initial_list.index('c') # To get the index of an element if the list, IF the element exists

#Better example

if 'first_end' in initial_list:
	start = initial_list.index('first_end')

if 'second_end' in initial_list:
	end = initial_list.index('second_end')

ss3 = initial_list[start+1:end]

import random
random.seed()

for i in range(0, 5):
	print initial_list[random.randint(0, len(ss3)-1) + (start+1)] # Print randomly only the values from the subset we want
