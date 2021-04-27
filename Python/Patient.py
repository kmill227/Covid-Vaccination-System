from User import User
from Insurance import Insurance
from Appointment import Appointment
from Vaccine import Vaccine
class Patient(User):
    
    def __init__(self):
        super.__init__() 
        self.ins = Insurance()
        self.vaccine = Vaccine()
        self.appointments = []

    def createAppointment(self):
        pass

    def followUpSchedule(self):
        pass

    def cancelAppointment(self):
        pass

    def rescheduleAppointment(self):
        pass

    
    