def wordcounter():
    sentence = input('> ')
    sent= sentence.split()
    words = len(sent)
    print('there are', words, 'words in your sentence!')
    vowels = ('a', 'i'
    consonants = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vc = sent.count(vowels)
    cc = sent.count(consonants)
    print('there are', vc, 'vowels and', cc, 'consonants in your sentence!')

wordcounter()