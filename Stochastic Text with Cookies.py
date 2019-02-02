from random import choice
subjects = ['COUNT', 'STRANGER', 'LOOK', 'CHURCH', 'CASTLE', 'PICTURE',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
Cookie = ['S\'more ', 'Thin Mint', 'Samoa', 'Tagalong', 'Trefoil', 'Do-Si- Do', 'Lemonade', 'Savannah Smile', 'Thanks-a-Lot', 'Toffee-Tastic', 'Caramel Chocolate Chip']
predicates = ['OPEN', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
              'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

i = 0
def phraseA():
    text = choice(operators) + ' ' + choice(Cookie)
    #if text == 'A EYE':
     #   text = 'AN EYE'
    return text + ' IS '
def phraseB():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
while i < 100:
    print('')
    print(phraseA() + choice(predicates) + choice(conjunctions) +
       phraseB() + choice(predicates) + '.')
    print i
    print(' \n')
    i+=1

