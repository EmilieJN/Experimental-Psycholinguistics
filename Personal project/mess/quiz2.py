def quiz2():
    q1 = 'do penguins have knees?'
    a1 = 'yes'
    q2='is the unicorn the national animal of Scotland?'
    a2 = 'yes'
    q3 = 'is the hybrid of a zebra and a horse called a hobra?'
    a3 = 'no'
    print(q1)
    if input('> ') == a1:
        print('correct! you got 1 point')
        print(q2)
        if input('> ')==a2:
            print('correct! you got 2 points')
            print(q3)
            if input('> ')==a3:
                print('correct! you got all 3 points!' )
            else:
                print('incorrect! you got 2 out of 3 points')
        else:
            print('incorrect! you got 1 point')
            print(q3)
            if input('> ')==a3:
                print('correct! you got 2 out of 3 points!' )
            else:
                print('incorrect! you got 1 out of 3 points')
    else:
        print('incorrect! you got 0 points')
        print(q2)
        if input('> ')==a2:
            print('correct! you got 1 point')
            print(q3)
            if input('> ')==a3:
                print('correct! you got 2 out of 3 points!' )
            else:
                print('incorrect! you got 1 out of 3 points')
        else:
            print('incorrect! you got 0 points')
            print(q3)
            if input('> ')==a3:
                print('correct! you got 1 out of 3 points!' )
            else:
                print('incorrect! you got 0 out of 3 points')


quiz2()