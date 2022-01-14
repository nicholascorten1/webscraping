from segments import *
import random
random.seed(1)

def set_user() -> str:
    """[summary]
    generates random slur from a fixed set of user for user compliant with ga analytics conventions
    """

    ## TODO --> create from a fixed list of users or set a seed to generate users corresponding to users in segmentss
    #nr_of_customers = 1000
    #seed_int = random.randint(0, nr_of_customers)

    """
    cookies exist of GA1.1 + 10 random ints on left side + . + 10 random ints on right side
    with segment I generated a number between 1 and 4 bc there are 4 types of users
    this segment number is the last number of the cookies right side ints
    """
    left_part = random.randint(1e9, 1e10-1)
    right_part = random.randint(1e8, 1e9-1)
    segment = random.randrange(1,5)

    user = f"{left_part}.{right_part}{segment}"
    print('user--', user)
    return 'GA1.1.' + user


"""
List_of_users is a fixed list with a length chosen in amount_of_users
the list consists of the cookies that were previously created
"""
list_of_users = []
amount_users = 10

for i in range(amount_users):
    ga_id = set_user()
    list_of_users.append(ga_id)


"""
list_of_users consists of the cookie for every user. the last number of every cookie is the segment the user belongs to.
so the if statement executes the website journey that matches for that type of user
"""

for j in range(len(list_of_users)):
    segment_type = eval(list_of_users[j][-1])
    if segment_type == 1:
        single_shopper_bevahiour()

    elif segment_type == 2:
        window_shopper_behaviour()

    elif segment_type == 3:
        researcher_behaviour()

    else:
        loyal_customer_behaviour()