import datetime
import Campus
import Vaccine
from DataBaseConnection import DataBase
class Appointment:
    def __init__(self):
        self.date = 0
        self.time = 0
        self.campus = 0
        self.userID = 0
        self.id = 0
        self.vaccine = Vaccine.Vaccine()
        self.complete = 0



    def createAppointment(self): 
        #log appointment in database
        db = DataBase()
        sql = "INSERT INTO appointment (UserID, Campus, AppointmentDate, AppointmentTime, VaccineBrand) VALUES (%s, %s, %s, %s, %s)"
        args = (self.userID, self.campus.name, self.date, self.time, self.vaccine.brand)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def followUpSchedule(self):
        # if brand is Moderna or pfizer, automatically schedules a second appointment, returns True if finished
        if self.vaccine.getBrand() == "Moderna":
            self.date = self.date + datetime.timedelta(days=28)
            self.createAppointment()
            return True
        elif self.vaccine.getBrand() == "Pfizer":
            self.date = self.date + datetime.timedelta(days=21)
            self.createAppointment()
            return True
        return False
        

    def cancelAppointment(self):
        # remove appointment from database 
        db = DataBase()
        sql = "DELETE FROM appointment WHERE AppointmentID = %s"
        args = (self.id, )
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def validDate(self, date):
        # return false if weekend, more than 2 weeks away, or if before current date
        if date.weekday() > 4:
            return False
        elif self.campus.lowVaccines() and date < self.campus.orderDate:
            return False
        elif date < datetime.date.today():
            return False
        elif date > datetime.date.today() + datetime.timedelta(days=14):
            return False 
        else:
            return True

    def setCampus(self, name):
        #set campus to hold data
        self.campus = Campus.Campus(name)
    
    def setDate(self, date):
        #set vaccine date
        self.date = date
    
    def getAvailableTimes(self):
        #retrieve available times from database, returns a list of all available times
        db = DataBase()
        sql = "SELECT AppointmentTime FROM appointment WHERE AppointmentDate=%s AND Campus =%s"
        args = (self.date, self.campus.name)
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

        return validAppointments

    def setTime(self, time):
        #set time of appointment
        self.time = time
        
    def getCampusBrand(self):
        #sets brand of vaccine given at appointment = to brand on hand at selected campus
       self.vaccine.setBrand(self.campus.getCurrentBrand()) 

    def setUserID(self, value):
        #set UserID of appointment to value
        self.userID = value

        