questions=["What is name of president of Pakistan?","How many provinces is in Pakistan?",
           "Who is CM Punjab?","Which countries are enemies of Pakistan?"]
answers=["Shehbaz Sharif","Five","Meryam Nawaz","India, Israil and America"]
t=0
for i in range(4):
    print(questions[i])
    a=input()
    if (a==answers[i]):
        t=t+100

print("Your score is :" , t)
