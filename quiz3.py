positive_answers = ['yes','Yes','True','true']
negative_answers = ['no','No','False', 'false']

questions = {
    'do penguins have knees?':positive_answers, 
    'is the unicorn the national animal of Scotland?':positive_answers,
    'is the hybrid of a zebra and a horse called a hobra?': negative_answers
}

def ask_question(question, correct_answers):
    print(question)
    answer = input('> ')
    if answer in correct_answers:
        print('correct!')
        return True
    else: 
        print('incorrect!')
        return False

def quiz():
    score = 0
    for question, correct_answers in questions.items():
        if ask_question(question, correct_answers):
            score = score + 1
    print('your final score is', score,'/ 3') 

quiz()  