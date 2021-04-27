import datetime
from Patient import Patient
from Employee import Employee
from Campus import Campus
class Appointment:
    def __init__(self):
        self.receiver = Patient()
        self.giver = Employee()
        self.date = datetime.date()
        self.time = datetime.time()
        self.campus = Campus()
        