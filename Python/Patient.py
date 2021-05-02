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
        self.appointments.append(Appointment.Appointment())
        self.appointments.append(Appointment.Appointment())
        self.dosesCompleted = 0

  



    
