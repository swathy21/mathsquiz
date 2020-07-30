print('$$$$$$$$ MATHS QUIZ $$$$$$$$')
import random
questions={}
score=0

for i in range(5):
    int_a=random.randint(10,99)
    int_b=random.randint(10,99)
    question=str(int_a)+' '+str('*')+' '+str(int_b)
    answer=eval(question)
    question+=':'
    questions.update({question:str(answer)})
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)!=str(user_answer):
        score+=1 
        print('incorrect')
    else:
        print('correct')
print('you'+' '+'got'+' '+str(score)+' '+'number'+' '+'incorrect')
