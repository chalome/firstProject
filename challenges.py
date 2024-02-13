#print 10 first natural number using while loop
'''x=0
while x!=10:
    x+=1
    print(x)'''
#printing the pattern
rows=6
#outer loop
'''for i in range(rows+1):
    #nested loop for columns
    for j in range(i):
        #dispaly number
        print('*',end='')
        #new line after each row
    print('')    '''
# outer loop
'''for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()'''
names = ['Kelly', 'Jessa', 'Emma']
# outer loop
'''for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()'''
'''rows=5
columns=3
for i in range(rows):
    for j in range(columns):
        print('*',end='')
    print()'''
sum=0;
number=int(input('Enter the number\n'))
for i in range(1,number+1):
    sum+=i
print(sum)