import datetime
import Patient
import Campus
class Appointment:
    def __init__(self):
        self.patient = Patient.Patient()
        self.date = datetime.date()
        self.time = datetime.time()
        self.campus = Campus.Campus()
        self.id = 0

    def createAppointment(self):
        pass
        

    def followUpSchedule(self):
        pass

    def cancelAppointment(self):
        pass
    
    def rescheduleAppointment(self):
        pass
        