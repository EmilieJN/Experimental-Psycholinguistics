def hangman():
    guess = input('> ')
    word = list('zebra')
    for letter in word:
        if guess in word:
            print('Good job,', guess, 'is in the word :)')
        else:
            print('Wrong,', guess, 'is not in the word :(')

hangman()