def g1():
    word = list('zebra')
    guess1= input('> ')
    if guess1 in word:
        print('Good job,', guess1, 'is in the word :)')
        return True
    else:
        print('Wrong,', guess1, 'is not in the word :(')
        return False

def g2():
    word = list('zebra')
    guess2= input('> ')
    if guess2 in word:
        print('Good job,', guess2, 'is in the word :)')
        return True
    else:
        print('Wrong,', guess2, 'is not in the word :(')
        return False

def g3():
    word = list('zebra')
    guess3= input('> ')
    if guess3 in word:
        print('Good job,', guess3, 'is in the word :)')
        return True
    else:
        print('Wrong,', guess3, 'is not in the word :(')
        return False

def g4():
    word = list('zebra')
    guess4= input('> ')
    if guess4 in word:
        print('Good job,', guess4, 'is in the word :)')
        return True
    else:
        print('Wrong,', guess4, 'is not in the word :(')
        return False

def g5():
    word = list('zebra')
    guess5= input('> ')
    if guess5 in word:
        print('Good job,', guess5, 'is in the word :)')
        return True
    else:
        print('Wrong,', guess5, 'is not in the word :(')
        return False

def hang():
    g1()
    g2()
    g3()
    g4()
    g5()
hang()