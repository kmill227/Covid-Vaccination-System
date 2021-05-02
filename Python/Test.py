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
hours = 8
minutes = 0
seconds = 0

for i in range(10):
    hours += 1
    minutes = 0
for i in range(6):
    validAppointments.append(datetime.time(hours, minutes, seconds))
    minutes += 10

for i in bookedAppts:
    print(i[0][1].time())


