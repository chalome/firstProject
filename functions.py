def add(a,b):
    return a+b
# m=add(4,5)
# print(m)
def checkoodEvenNumber(number):
    if number%2==0:
        return True
    else:
        return False
number=int(input('Enter a number to check:\n'))
if checkoodEvenNumber(number):
    print('it is even')
else:
    print("it is ood")