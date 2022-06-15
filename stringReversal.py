def string_operations(string1, string2, string3):  # creating function to call later
    reversed_string = string3[::-1] + ' ' + string2[::-1] + ' ' + string1[::-1]  # ::-1 slice reverses string
    return reversed_string  # returning value to print later


str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
str3 = input('Enter the third string: ')

# prints the return value of the called string_operations function

if __name__ == '__main__': # added main method with a while loop to keep program running and see output before it closes
    print('Your three strings in reverse order:', string_operations(str1, str2, str3))
    x=1
    while x == 1:
        x = input('Enter anything to quit: ')