def run():
    # First make commands
    base  = ""
    # Now it dosent understand 'exit'

    while True:
        base = input('base > ').lower()
# This is weird
        if base == 'func void (); {':
            print('Void function')

        elif base == 'hello':
            print('Hello')
        
        if base == 'commands':
            while base != 'exit':
                base = input('cmd > ')

        if base == '':
            print('Dont understand empty strings!!')
        
        # Add an exit script

        if base == 'exit':
            break

        # Add error message!

        else:

            print(f'Invalid command {base}')