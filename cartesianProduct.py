def cartesianProduct(a, b):
    print("Cartesian product of your two lists:\n")
    return [(x, y) for x in a for y in b]


if __name__ == '__main__':
    print("This program will take your input of 10 integers to create list 1, another 10 for list 2, then find "
          "the cartesian product of both lists.\n")
    list1 = []
    temp = 0
    while temp < 10:
        list1.append(int(input("Enter in integer #" + str(temp+1) + " (only integers!) for list 1, one by one: ")))
        temp += 1

    list2 = []  # added another loop for user to enter values for list 2
    temp = 0
    while temp < 10:
        list2.append(int(input("Enter in integer #" + str(temp + 1) + " (only integers!) for list 2, one by one: ")))
        temp += 1
    print(cartesianProduct(list1, list2))
    temp = 1
    while temp == 1:
        temp = input('Enter anything to quit: ')
