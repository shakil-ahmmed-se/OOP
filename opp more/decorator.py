import math

def timer(func):
    def inner(*args , **kwargs):
        print('Time start')
        # print(func)
        func(*args, **kwargs)
        print('Time end')
    return inner

# timer()()

@timer
def get_factorial(n):
    print('Factorial Starting')
    result = math.factorial(n)
    print(f'Factoral of n is {result}')

get_factorial(n=8)