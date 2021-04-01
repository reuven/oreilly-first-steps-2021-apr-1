def menu(*args):  # args is a tuple containing all passed arguments
    while True:
        choices = '/'.join(sorted(args))
        user_choice = input(f'Enter your choice ({choices}): ')

        if user_choice in args:
            return user_choice

        # f-string, evaluates stuff in {}
        print(f'Hey! {user_choice} was not in args!')


if __name__ == '__main__':
    user_choice = menu('a', 'b', 'c')
    