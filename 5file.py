#!/usr/bin/python3

SECRET = 'xpto'

while True:
    passowrd = input('Please enter your password: ')
    if not password:
        continue
    elif password == SECRET:
        break

    print('Wrong password!')


print('Welcome!')
