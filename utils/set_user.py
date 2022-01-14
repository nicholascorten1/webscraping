import random
random.seed(1)


def create_user() -> str:
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
