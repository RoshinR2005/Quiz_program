import mysql.connector as ms
import datetime

con = ms.connect(host="localhost", user="root", passwd="admin", database="Quiz")
cur = con.cursor()
name = input("Enter your Name: ")

print("Welcome " + name + " To Catechize: The Quiz Master")
cur.execute(
    "CREATE TABLE CATECHIZE (qid INT PRIMARY KEY, Question VARCHAR(1000), Option_A VARCHAR(100), Option_B VARCHAR(100), Option_C VARCHAR(100), Option_D VARCHAR(100), Answer VARCHAR(100), Category varchar(100))"
)
cur.execute(
    "INSERT INTO CATECHIZE VALUES(1,'Data structures are','Network structures','Group of data','Different types of data','Different operations on data','B','IT')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(2,'Which of the following is/are linear data structure(s)','Array','Stack','Queue','All of these','D','IT')"
)
con.commit()
cur.execute("INSERT INTO CATECHIZE VALUES(3,'Process of inserting an element in stack is called','Create','Push','Evaluation','Pop','B','IT')")
con.commit()
cur.execute("INSERT INTO CATECHIZE VALUES(4,'Process of removing an element from stack is called','Create','Push','Evaluation','Pop','D','IT')")
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(5,'Which data structure is needed to convert infix notation to postfix notation?','Branch','Tree','Queue','Stack','D','IT')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(6,'What does the Olympic Flame symbolize?','Zeal to play sports','Challenge','Continuity','Integrity','C','SPORTS')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(7,'The famous football player Maradona belongs to which among the following countries?','Brazil','Chile','Argentina','Italy','C','SPORTS')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(8,'Euro Cup is related to which sports?','Badminton','Football','Table Tennis','Hockey','B','SPORTS')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(9,'Murugappa Gold Cup is related to which among the following sports?','Hockey','Football','Cricket','Table Tennis','A','SPORTS')"
)
con.commit()
cur.execute(
    "INSERT INTO CATECHIZE VALUES(10,'What is the standard width of each wicket in cricket?','9 inches','10 inches','11 inches','12 inches','A','SPORTS')"
)
con.commit()
score = 0
category = input("Select from the following categories (IT/SPORTS): ")
cur.execute(
    " SELECT qid,Question ,Option_A, Option_B,Option_C,Option_D,Answer FROM CATECHIZE WHERE Category='"
    + str(category.upper())
    + "'"
)
for x in cur:
    qs_id = x[0]
    qs_ans = x[6]
    print(x[1])
    print("\nOptions:")
    print("Option A:", x[2])
    print("Option B:", x[3])
    print("Option C:", x[4])
    print("Option D:", x[5])
    ans = input("Select your choice (A/B/C/D):")
    myans = ans.upper()
    print("Correct answer is option", qs_ans)
    if myans == qs_ans:
        score = score + 1

dt = datetime.datetime.now()
dtQuiz = dt.strftime("%d-%b-%Y")
with open('CATECHIZE _score.txt', 'a') as f:
    f.write('\n')
    f.write('Date Attended :' + dt.strftime("%d-%b-%Y"))
    f.write('\n')
    f.write('Name of User :' + name)
    f.write('\n')
    f.write('Score:' + str(score))
print("Your total Score is: ", score)
ans = input("Do you want to contribute? (y,n): ")
while ans == 'y' or ans == 'Y':
    cur.execute("SELECT IFNULL(MAX(qid),0)+1 AS qid FROM CATECHIZE")
    for x in cur:
        qid = x[0]
    cat = input("Enter category (IT/SPORTS): ")
    cat.upper()
    q = input("Enter the question: ")
    o1 = input("Enter the first option: ")
    o2 = input("Enter the second option: ")
    o3 = input("Enter the third option: ")
    o4 = input("Enter the fourth option: ")
    oc = input("Enter the correct option: ")
    sql = "insert into CATECHIZE(qid,Question ,Option_A,Option_B,Option_C,Option_D,Answer,Category)values({},'{}','{}','{}','{}','{}','{}','{}')".format(
        qid, q, o1, o2, o3, o4, oc, cat
    )
    cur.execute(sql)
    con.commit()
    ans = input("Do you want to continue? (y/n): ")
