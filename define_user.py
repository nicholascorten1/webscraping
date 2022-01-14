import random

random.seed(1)

list_of_users = []

for i in range(10):
    segment = random.randint(1,5)
    list_of_users.append(segment)

print(list_of_users)
