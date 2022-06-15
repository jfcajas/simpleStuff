x = 0
total = 0
floats = []
interest_value = 0.0

print("Enter in 5 floating-point values to receive some analysis on the given values")
print("do not enter non-floats values like a string...")

while x < 5:  # while loop to get 5 inputs from user
    floats.append(float(input("Enter the next floating-point value: ")))
    x += 1 # above line changes user string input into float, and warns user not to use non-float values

for x in floats:  # for loop to get total by adding each value in floats list
    total += x
interest_values = [(x+(x*0.2)) for x in floats]  # performs math on each value in floats list with a for loop

avg = total/len(floats)  # simple total / length for average

print('Total: ', total)
print('Average: ', avg)
print('Min value: ', min(floats))  # using min method
print('Max value: ', max(floats))  # using max method
print('Values with 20% interest: ', interest_values)
