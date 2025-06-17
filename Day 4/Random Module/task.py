import random
import my_module

random_integer = random.randint(0, 1)
print(random_integer)
if random_integer == 0:
    print("Heads")
else:
    print("Tails")

ran_int = random.randint(0, 10)
print(my_module.my_favorite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)