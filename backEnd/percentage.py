import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database='myBuddyDb')

studentCursor = mydb.cursor()
studentCursor.execute("SELECT StudentID FROM STUDENTS;")

studentIds = studentCursor.fetchone()

studentList = []
mentorList = []

while studentIds is not None:
	studentList.append(studentIds[0])
	studentIds = studentCursor.fetchone()


studentCursor.close()

mentorCursor = mydb.cursor()
mentorCursor.execute("SELECT MentorID FROM MENTORS;")

mentorIds = mentorCursor.fetchone()

while mentorIds is not None:
	mentorList.append(mentorIds[0])
	mentorIds = mentorCursor.fetchone()
	

mentorCursor.close()

i = 0
interestsCount =[]
#studentMentorPercentile = [[],[]]


studentMentorPercentile = []
for k in range(len(studentList)):
    studentMentorPercentile.append([0] * len(mentorList))
	

while i < len(studentList):
	j = 0
	mentorPercentile = []
	while j < len(mentorList):
		interestsName = []
		interestsCursor = mydb.cursor()
		interestsCursor.execute("SELECT InterestTitle FROM STUDENT_INTERESTS NATURAL JOIN MENTOR_INTERESTS WHERE StudentID="+str(i)+" AND MentorID="+str(j)+" AND STUDENT_INTERESTS.InterestTitle = MENTOR_INTERESTS.InterestTitle")		
		interestsName.append(interestsCursor.fetchall())
		matchingInterests = len(interestsName[0])
		#interestsCount.append(len(interestsCursor.fetchall()))
		interestsCursor.close()
		print(interestsName)
		print("matching interests"+str(matchingInterests))
		interestsNameTwo = []
		interestsCursor = mydb.cursor()
		interestsCursor.execute("SELECT a.firstInterest from(SELECT StudentID, SIMILAR_INTERESTS.firstInterest FROM STUDENT_INTERESTS JOIN SIMILAR_INTERESTS WHERE StudentID="+str(i)+" AND (STUDENT_INTERESTS.interestTitle=SIMILAR_INTERESTS.secondInterest)) as a JOIN MENTOR_INTERESTS WHERE MentorID="+str(j)+" AND (a.firstInterest=MENTOR_INTERESTS.interestTitle)")		
		interestsNameTwo.append(interestsCursor.fetchall())
		interestsCursor.close()
		interestsCursor = mydb.cursor()
		interestsCursor.execute("SELECT a.secondInterest from (SELECT StudentID, SIMILAR_INTERESTS.secondInterest FROM STUDENT_INTERESTS JOIN SIMILAR_INTERESTS WHERE StudentID="+str(i)+" AND (STUDENT_INTERESTS.interestTitle=SIMILAR_INTERESTS.firstInterest)) as a JOIN MENTOR_INTERESTS WHERE MentorID="+str(j)+" AND (a.secondInterest=MENTOR_INTERESTS.interestTitle)")		
		interestsNameTwo.append(interestsCursor.fetchall())
		interestsCursor.close()
		similarInterests = len(interestsNameTwo[0])
		print("similarInterests"+str(similarInterests))
		
		interestsNameTotal = []
		interestsCursor = mydb.cursor()
		interestsCursor.execute("SELECT InterestTitle FROM STUDENT_INTERESTS WHERE StudentID="+str(i)+"")		
		interestsNameTotal.append(interestsCursor.fetchall())
		totalInterests = len(interestsNameTotal[0])
		interestsCursor.close()	
		print("totalInterests"+str(totalInterests))
		
		#mentorPercentile.append(100*(matchingInterests+0.5*similarInterests)/totalInterests)		
		studentMentorPercentile[i][j] = 100*(matchingInterests+0.5*similarInterests)/totalInterests		
		j = j + 1
	#studentMentorPercentile[i].append(mentorPercentile)	
	i = i + 1

	
for k in range(len(studentList)):
	print(studentMentorPercentile[k])
