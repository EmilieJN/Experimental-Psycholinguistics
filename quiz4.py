positive_answers = ['yes','Yes', 'y', 'True','true']
negative_answers = ['no','No','n', 'False', 'false']

def q1():
    qp= 'Do penguins have knees?'
    print(qp)
    answer = input('> ')
    if answer in positive_answers:
        print('Correct!')
        return True
    else:
        print('Incorrect!')
        return False

def q2():
    qu= 'Is the unicorn the national animal of Scotland?'
    print(qu)
    answer = input('> ')
    if answer in positive_answers:
        print('Correct!')
        return True
    else:
        print('Incorrect!')
        return False

def q3():
    qz= 'Is the hybrid of a zebra and a horse called a hobra?'
    print(qz)
    answer = input('> ')
    if answer in negative_answers:
        print('Correct!')
        return True
    else:
        print('Incorrect!')
        return False

def quiz():
    score1 = q1()
    score2 = q2()
    score3 = q3()
    list=[score1,score2,score3]
    print('Good job, your final score is', list.count(True), '/ 3!')
    

quiz()  