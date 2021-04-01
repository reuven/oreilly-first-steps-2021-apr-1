import random   # here, mymod is importing random

# if __name__ == '__main__':  # Python sets __name__'s value, whether "__main__" or something else
#     print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]

z = {'a': 1, 'b': 2, 'c': 3}


def hello(name):
    return f'Hello, {name}!'


# stuff below this line, and this "if" statement, will only execute
# when the module is run as a standalone program.  When it is 
if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')
