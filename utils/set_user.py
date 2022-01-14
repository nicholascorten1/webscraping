import random

def set_user() -> str:
    """[summary]
    generates random slur from a fixed set of user for user compliant with ga analytics conventions
    """

    ## TODO --> create from a fixed list of users or set a seed to generate users corresponding to users in segmentss
    nr_of_customers = 1000
    seed_int = random.randint(0, nr_of_customers)

    left_part = random.randint(1e9, 1e10-1)
    

    right_part = random.randint(1e9, 1e10-1)
    user = f"{left_part}.{right_part}"
    print('user--', user)
    return 'GA1.1.' + user
    
set_user()