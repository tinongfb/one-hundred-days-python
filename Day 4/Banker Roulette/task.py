import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

payer_random = random.choice(friends)
print(payer_random)

payer_rand_index = random.randint(0, 4)
print(friends[payer_rand_index])