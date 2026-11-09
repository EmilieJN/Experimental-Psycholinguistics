def count():
    sentence = input()
    for word in sentence:
        print('there are', len(sentence), 'letters in', sentence)

count()