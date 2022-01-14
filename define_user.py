import random
import numpy as np
random.seed(1)

""" list_of_users = []

for i in range(10):
    segment = random.randint(1,5)
    list_of_users.append(segment)

print(list_of_users) """

x = np.random.randint(1,5, size=10)
print(x[0])
