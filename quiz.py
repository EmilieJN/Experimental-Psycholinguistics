questions = [{'question': 'do penguins have knees?','answer' : 'yes'}, 
{'question':'is the unicorn the national animal of Scotland?', 'answer':'yes'},
{'question':'is the hybrid of a zebra and a horse called a hobra?', 'answer':'no'}]

def quiz():
    for i in range(len(questions)): 
        print(questions[i]["question"])        
        for j in range(len(questions)):
            for key, val in questions[j].items():
                if key == "answer":
                    val == 'correct'
    if input() == val:
        print('correct!')
    else:
        print('incorrect!')
quiz()