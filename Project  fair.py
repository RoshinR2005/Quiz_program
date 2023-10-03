import mysql.connector as ms
import datetime
con=ms.connect(host="localhost",user="root",passwd="admin",database="Quiz")
cur=con.cursor()

name=input(" Enter  your Name :")
print( "Welcome  " + name)
category=input("Select from the following categories (IT/SPORTS) : ")
score=0

cur.execute(" SELECT  id,Question ,Option_A, Option_B,Option_C,Option_D,Answer  FROM  CATACHIZE  WHERE Category='" +str(category.upper())+ "'" )
for x in cur:
    qs_id=x[0]
    qs_ans=x[6]
    print(x[1])
    print("\nOptions:")
    print("Option A :",x[2])
    print("Option B :",x[3])
    print("Option C :",x[4])
    print("Option D :",x[5])
    ans=input("Select your choice (A/B/C/D):")
    myans=ans.upper()
    print("Correct answer is option",qs_ans )
    if  myans==qs_ans:
        score= score+1

        
dt = datetime.datetime.now()
dtQuiz=dt.strftime("%d-%b-%Y")


with open('CATACHIZE _score.txt', 'a') as f:
    f.write('\n')
    f.write('Date Attended :' +   dt.strftime("%d-%b-%Y"))
    f.write('\n')
    f.write('Name of User :' +name)
    f.write('\n')
    f.write('Score:' +str(score))

print("Your total Score is: ",score)
