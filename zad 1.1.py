namesList = str(input('Wprowadź listę imion używając przecinku lub spacji: '))

for i in namesList.split(' '):
    if i == ' ' or i == '':
        continue
    else:
        for j in i.split(','):
            print('Hi', j)
