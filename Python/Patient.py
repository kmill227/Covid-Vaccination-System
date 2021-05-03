import User
import Appointment
import Vaccine
import Insurance
from DataBaseConnection import DataBase
import datetime

class Patient(User.User):
    
    def __init__(self):
        super().__init__() 
        self.vaccine = Vaccine.Vaccine()
        self.appointments = []
        self.insurance = Insurance.Insurance()
        
  
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
        db.connection.close()

    def numberOfAppointments(self):
        self.loadAppointments()
        return len(self.appointments)

    def isEligible(self):
        if self.numberOfAppointments() == 1 and self.appointments[0].vaccine.brand == "Johnson&Johnson":
            return False
        elif (self.numberOfAppointments() == 2) and (self.appointments[0].vaccine.brand == "Pfizer" or self.appointments[0].vaccine.brand == "Moderna"):
            return False
        else:
            return True
    
    def setInsurance(self, value):
        self.insurance.policyNum = value

    def insertAppointment(self, appointment):
        self.appointments.append(appointment)

    def logData(self):
        db = DataBase()
        


