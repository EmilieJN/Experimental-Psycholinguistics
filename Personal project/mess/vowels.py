vowels = ['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def vowel():
    sentence = input('> ')
    
    if vowels in sentence:
        print('vowels')
        return True
    else:
        print('no vowels')
        return False

vowel()