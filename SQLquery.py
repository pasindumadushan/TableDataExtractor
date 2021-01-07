import sqlite3
import matplotlib.pyplot as plt

def insertRecord(AttendentSheet):

    with sqlite3.connect("AttendenceSheet.db") as db:
        cursor = db.cursor()
    Cursor = db.cursor()

    #cursor.execute("DELETE FROM sheet")

    for i in range(len(AttendentSheet)):

        insertQuery = """INSERT INTO sheet(StudentNo,Title,StudentName,Signature) 
        VALUES(?,?,?,?);"""

        data_tuple = (AttendentSheet[i][3], AttendentSheet[i][2], AttendentSheet[i][1], AttendentSheet[i][0])
        cursor.execute(insertQuery, data_tuple)
        db.commit()

    cursor.execute("SELECT * FROM sheet")
    i=cursor.fetchall()
    for j in i:
        print(j)

    cursor.execute("SELECT StudentNo,COUNT(StudentNo) FROM sheet WHERE Signature = 'true' GROUP BY StudentNo ORDER BY StudentNo")
    rows = cursor.fetchall()

    StudenId = []
    Days = []
    for row in rows:
        StudenId.append(row[0])
        Days.append(row[1])

    fig, ax = plt.subplots()
    ax.bar(StudenId, Days)
    # set title and labels
    ax.set_title('Attendence')
    ax.set_xlabel('Student Id')
    ax.set_ylabel('Number of days')

    plt.show()



