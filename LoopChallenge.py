'''line_to_print = ''
for i in range (1, 10):
    for j in range (0, 9):
        line_to_print += str(i)
    print(line_to_print)
    line_to_print = ''
    '''
countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']
for country in countries:
    print(country, 'contains', len(country), 'letters!')