def menu(*args):  # args is a tuple containing all passed arguments
    while True:
        user_choice = input('Enter your choice: ')

        if user_choice in args:
            return user_choice

        print(f'Hey! {user_choice} was not in args!')
