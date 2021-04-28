import datetime
from Patient import Patient
from Employee import Employee
from Campus import Campus
class Appointment:
    def __init__(self):
        self.patient = Patient()
        self.date = datetime.datetime()
        self.campus = Campus()
        