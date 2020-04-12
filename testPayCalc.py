#Payroll Program
#james Page January 23, 2020

hours = input('Enter the number of hours worked: ')
rate = input('Enter the rate of pay: ')

hours = float(hours)
rate = float(rate)

try:
    pay = hours * (rate * 1.5)
    print('Gross Pay: ',pay)
    
except:
    print('Please enter a numeric value')