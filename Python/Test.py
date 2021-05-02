from DataBaseConnection import DataBase
import datetime


db = DataBase()
date = datetime.date(2021,5,3)
campus = "Stark"
sql = "SELECT AppointmentTime FROM appointment WHERE AppointmentDate=%s AND Campus =%s"
args = (date, campus)
db.cursor.execute(sql, args)
bookedAppts = db.cursor.fetchall()



validAppointments = []
k = 0
seconds = 28800

for i in range(60):
    validAppointments.append(datetime.timedelta(seconds = seconds))
    seconds += 600 

for i in range(len(bookedAppts)):
    temp = bookedAppts[i][0]
    for j in validAppointments:
        if j == temp: 
            validAppointments.remove(j)
















