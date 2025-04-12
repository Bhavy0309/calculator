age=input("enter your age")
age_to_vote=18
vote=2
result=1
if (int(age)<age_to_vote):
 print("you are young to vote, vote when you are 18")
else:
   print("you are eliggible to vote")
   to=input("who do you vote to? Trump or Bidden. For voting Bidden enter 4. For voting Trump enter 3. ")
   print("we have received your vote. results will come in latter.")
   check=input("results are in.if you want to see who won then enter 8 ")
   if(int(check)==8 and int(to)==3):
    print("Trump has won! congarts Trump voters!") 
   elif(int(check)==8 and int(to)==4):
     print("Bidden has won! congrats Bidden voters")
### int=intgers like 1,2,3,4.....
### input means what you put.

#vote_one=input("")
#if(vote<int(vote_one)):

#resultone=input("enter integer value more than one")   
#if(result<int(resultone)):
   



   
   