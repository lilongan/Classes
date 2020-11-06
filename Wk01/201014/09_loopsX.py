i = 0

while i <= 10:
    print(i)
    # i += 1
    i = i + 1

i = 10

while i <= 10 and i > 0:
    print(i)
    i -= 1

secret_password = ''
secret_username = ''
chances = 1

while secret_password != 'abcd1234' and secret_username != 'RSWes' and chances < 4:
    secret_username = input('Username: \n')
    secret_password = input('Password: \n')

    if secret_password != 'abcd1234' or secret_username != 'RSWes':
        chances += 1
        if chances > 3:
            print('Too many attempts. Byeeeeeeee')
        else:
            print('Incorrect credentials. Please try again.')
    else:
        print('Welcome to Skynet, Mr. Connor')
