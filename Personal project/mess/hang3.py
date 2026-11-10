def hangy():
    word = list('zebra')
    word_length = len(word)
    letters = (' _ '*word_length)
    print(letters)
    guess = input('Guess! > ')
    letters_guessed = []
    your_word = ""
    number_of_lives = 6
    
    for letter in word:
        if letter == guess:
            your_word  = your_word + letter
            letters_guessed.append(guess)
        elif letter in letters_guessed:
            your_word  = your_word + letter
        else:
            your_word = your_word + "_"

hangy()