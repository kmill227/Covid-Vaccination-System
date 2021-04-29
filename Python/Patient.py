from User import User
from Insurance import Insurance
from Appointment import Appointment
from Vaccine import Vaccine
from DataBaseConnection import DataBase
class Patient(User):
    
    def __init__(self):
        super.__init__() 
        self.ins = Insurance()
        self.vaccine = Vaccine()
        self.appointments = []
        self.name = ""

    def createAppointment(self):
        pass

    def followUpSchedule(self):
        pass

    def cancelAppointment(self):
        cancel = DataBase()
        cancel.connection.cursor.execute(
            "SELECT * FROM user WHERE ID = appoint user id"
            
            
            )

    def rescheduleAppointment(self):
        pass

    
    