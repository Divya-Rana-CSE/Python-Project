# know your country game:
from random import shuffle
ques = [
    ("What is name of your country","india"),
    ("What is the capital of your country","new delhi"),
    ("What is the your national flower","lotus"),
    ("What is the name of your national animal",'tiger'),
    ("What is your national bird's name","peacock"),
    ("What is your national color",'saffron')
]
shuffle(ques)
right = 0
wrong = 0
for question, right_ans in ques:
    ans = input(question + ' ')
    if ans.lower() == right_ans:
        right +=1
    else:
        print("No the right ans is:", right_ans)
        wrong +=1
print("Congratulation !")
print("You gave", right,"right answers and", wrong ,"wrong answers")