import User
import Campus
class Admin(User.User): 

    def __init__(self): 
        super.__init__()

    def retrieveAllAppointments(self):
        # returns a list with all appointments from all campuses retrieved from the database
        pass

    def logVaccine(self, Appointmentid, UserID):
        #returns nothing, changes values for user and appointment in database when an appointment is complete 
        pass

    def registerUser(self):
        # creates a new login in the database 
        pass


