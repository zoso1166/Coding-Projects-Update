# Number Test by James Page

total = 0                            # Initialize total and count variables
count = 0
nums = []

while (True):
    inp = input('Enter a number: ')  # User input
    if inp == 'done': break          # Tests for end of user input
    value = float(inp)               # Converts user input from string to floating-point
    nums.append(inp)
    total = total + value            # Adds user input to total
    count = count + 1                # Increments number of operands by 1
    print(nums)

print('Total:', total)               # Returns calculated values
print('Count:', count)
print('Minimum number: ', min(nums))
print('Maximum number: ', max(nums))
