questions = ['Do you love God?', 'Do you accept jesus christ as your lord and saviuor?']

answers = ['yes', 'yes', 'no', 'no', 'yes']

score = 0

def quizGame():
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        ans = input('Please answer: \n')
        if ans == answers[i]:
            print("Correct")
            score += 1
        else:
            print('Incorrect, you repent!')
    print(f'Final Score: {score} ')

quizGame()




quizGame()