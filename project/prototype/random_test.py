import random
random.seed()
n_of_jumps = random.randint(1, 7)
list_of_links_id = []
for j in range(0, n_of_jumps): list_of_links_id.append(random.randint(0, 100))
print list_of_links_id
for id in list_of_links_id: print id % 10