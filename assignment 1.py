#Q1
no_1 = int(input("enter 1st no. : "))           #asking for three inputs from user 
no_2 = int(input("enter 2nd no. : "))
no_3 = int(input("enter 3rd no. : "))

Average = (no_1 + no_2 + no_3)/3              #average of three numbers
print('average of three numbers is =', Average)

#Q2
gross_income = float(input("enter gross income to the nearest penny: "))
std_deduction = 10000 
dependent_deduction = 3000
num_dependent = int(input("Enter number of dependents:"))
taxable_income = gross_income - std_deduction - (dependent_deduction * num_dependent)
tax_rate = 0.2
tax = (taxable_income * tax_rate)
print("income tax:",tax) 




#Q3
Seconds = int(input("enter number of seconds: "))

minutes = Seconds//60  # for minutes
sec = Seconds % 60
print("That's",minutes,'minutes and',sec,'seconds')

#Q4

number1= '25'
number2= 25
number3= 25.0

result= str(int(number1) + number2 + int(number3))
print(result)


#Q5

import math
for i in range(0,360,15):
    sin = math.sin(i*math.pi/180)
    cos = math.cos(i*math.pi/180)
    print(i,'---',round(sin,4),round(cos,4))