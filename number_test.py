# Number Test by James Page

total = 0                            # Initialize total and count variables
count = 0

while (True):
    inp = input('Enter a number: ')  # User input
    if inp == 'done': break          # Tests for end of user input
    value = float(inp)               # Converts user input from string to floating-point
    total = total + value            # Adds user input to total
    count = count + 1                # Increments number of operands by 1

average = total / count              # Calculates total divided by count

print('Total:', total)               # Returns calculated values
print('Count:', count)
print('Average:', average)