from User import User
from Insurance import Insurance
from Appointment import Appointment
from Vaccine import Vaccine
from DataBaseConnection import DataBase
import datetime

class Patient(User):
    
    def __init__(self):
        super.__init__() 
        self.ins = Insurance()
        self.vaccine = Vaccine()
        self.appointments = []
        self.name = ""

    def createAppointment(self):
        create = DataBase(
        CampusData = input("Select Campus")
        VaccineData = cursor.fetchone()[5]


        DateData = input("Select Appointment Date")
        create.connection.cursor.execute(
            "SELECT * FROM appointment WHERE Campus = (%s) AND AppointmentDate = (%s)",
            (CampusData, DateData)
        )

        AvailableTimes = 
        TimeData = input("Select Appointment Time")

        create.connection.cursor.execute(
            "INSERT INTO appointment (AppointmentTime, AppointmentDate, UserID, Campus, VaccineBrand) VALUES (%s, %s, %s, %s, %s)",
            (TimeData, DateData, self.id, CampusData, )
        )

    def followUpSchedule(self):
        pass

    def cancelAppointment(self):
        cancel = DataBase()
        cancel.connection.cursor.execute(
            "SELECT * FROM user WHERE ID = appoint user id"
            
            
            )

    def rescheduleAppointment(self):
        pass

    
    