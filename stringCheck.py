def stringCheck():
    S = input('Input a string less than 50 characters: ')  # takes input from user

    if len(S) > 50:
        print('That string is too long, run the program and try again')  # if string is too long, will exit program
        exit()
    if any(letter.isalnum() for letter in S):
        print('Does the string contain alphanumeric characters?: ', True)  # these if statements use the any() method to
    else:
        print('Does the string contain alphanumeric characters?: ', False)  # check if any of the characters of each

    if any(letter.isalpha() for letter in S):
        print('Does the string contain alphabetical characters?: ', True)  # string contain what we are looking for
    else:
        print('Does the string contain alphabetical characters?: ', False)  # then prints whether the statements are T/F

    if any(letter.isdigit() for letter in S):
        print('Does the string contain digits?: ', True)
    else:
        print('Does the string contain digits?: ', False)

    if any(letter.islower() for letter in S):
        print('Does the string contain lower case characters?: ', True)
    else:
        print('Does the string contain lower case characters?: ', False)

    if any(letter.isupper() for letter in S):
        print('Does the string contain upper case characters?: ', True)
    else:
        print('Does the string contain upper case characters?: ', False)


stringCheck()
