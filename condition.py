score=input("enter your score: ")
pass_mark=50
limit=100
if(limit<int(score)):
    print("cheated. try agian")
elif(int(score)>pass_mark):
    print("passed exams")
else:
    print("try again")

