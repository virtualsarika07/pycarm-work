num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
print('type 1 for addition,\n type 2 for multiplication,\n type 3 for Division,\n type 4 for subtraction')
operator = int(input('Enter your option:'))

if operator ==1:
    if num1==56 and num2==9:
        print("Theb sum of numbers is:",77)
    else:
        print("Sum of two numbers is:",num1+num2)

elif operator == 4:
    print("subtraction of two numbers is:",num1-num2)

elif operator == 2:
    if num1 == 45 and num2 == 3:
        print("multiplication of  two numbers is:",555)
    else:
        print("multiplication of  two numbers is:",num1*num2)

elif operator == 3:
    if num1 == 56 and num2 == 6:
        print("Divion of two number is:",4)
    else:
        print("Divion of two number is:", num1%num2)

else:
    print("invalid operator")


