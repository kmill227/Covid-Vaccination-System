from Vaccine import Vaccine
from Insurance import Insurance 
class Patient:

    def __init__(self):
        self.email = " "
        self.password = " "
        self.vaccine = Vaccine()
        self.insurance = Insurance()
        self.appointments = {}
    
    