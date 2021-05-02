import datetime
import Campus
import Vaccine
class Appointment:
    def __init__(self):
        self.date = 0
        self.time = 0
        self.campus = 0
        self.id = 0
        self.vaccine = Vaccine.Vaccine()
        self.complete = 0

    def createAppointment(self, date, time, campus):
        #logs appointment to database
        pass

    def followUpSchedule(self):
        # if brand is Moderna or pfizer, prompts user to schedule a second appointment
        pass

    def cancelAppointment(self):
        # remove appointment from database 
        pass
    
    def rescheduleAppointment(self):
        #remove from database and add new appointment from user input from menu 
        pass
        