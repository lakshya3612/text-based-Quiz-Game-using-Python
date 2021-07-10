import random
scores=0
print("welcome to the coder lakshya's grand quiz")
riddle={}
with open("riddles.txt",'r')as f:
    questions=f.readlines()
    for question in questions:
        q,a=question.strip().split(':')
        riddle[q]=a
        #print the rules
print("*********RULES*********")
print("maximum question asked=5")
print("correct answer=2 marks")
print("wrong answer=-1 marks")
while True:
    add_question=input("do you want to add any question y/Y/n/N")
    if add_question=='y' or add_question=='Y':
        ques=input("enter the question")
        answer=input("enter the answer of the question")
        riddle=[ques]=answer
    else:
        break
#initialise the questions asked count
qcount=0
#get keys all keys from riddles and convert to list
questions=list(riddle.keys())
#shuffle the list
random.shuffle(questions)
#read each question from the list
for q in questions:
    print(q)
    ans=input("enter your answer")
    #compare both answers by converting to same case and update and print score
    if ans.upper()==riddle[q].upper():
        print("correct answer")
        scores+=2
    else:
        print("better luck next time")
        scores-=1
    print(scores)
    #increment question count and exit if 5 questions asked
    qcount+=1
    if qcount==5:
        break
print("end of quiz")
print("total score=",scores)

    

    
