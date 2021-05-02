import User
import Insurance
import Appointment
import Vaccine
from DataBaseConnection import DataBase
import datetime

class Patient(User.User):
    
    def __init__(self):
        super().__init__() 
        self.ins = Insurance.Insurance()
        self.vaccine = Vaccine.Vaccine()
        self.appointments = []
        self.dosesCompleted = 0

  
    def loadAppointments(self):
        #loads Appointments from database for given user 
        db = DataBase()
        sql = "SELECT * FROM appointment WHERE UserID = %s"
        args = (self.id, )
        db.cursor.execute(sql, args)
        apptList = db.cursor.fetchall()
        for i in range(len(apptList)):
            self.appointments.append(Appointment.Appointment())
            self.appointments[i].id = apptList[i][0]
            self.appointments[i].campus = apptList[i][2]
            self.appointments[i].date = apptList[i][3]
            self.appointments[i].time = apptList[i][4]
            self.appointments[i].vaccine.brand = apptList[i][5]
            self.appointments[i].complete = apptList[i][6]

patient = Patient()
patient.id = 1000
patient.loadAppointments()
for i in patient.appointments:
    print(i.id, ' ', i.campus, ' ', i.date, ' ', i.time, ' ', i.vaccine.brand, ' ', i.complete)



    
