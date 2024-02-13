print('My calculator...')
number1=int(input("Enter number one\n"))
operator=input('Enter the operator:(+,-,*,/)\n')
number2=int(input("Enter number two\n"))
result=0
def show_result():
    print(f'{number1}{operator}{number2}={result}')
if operator=='+':
   result=number1+number2
   show_result()
elif operator=='-':
     result=number1-number2
     show_result()
elif operator=='*':
     result=number1*number2
     show_result()
elif operator=='/':
    if number2>0: 
       result=number1/number2
       show_result()
    else:
        print('Division by zero does not exist....')   
