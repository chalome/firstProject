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
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()