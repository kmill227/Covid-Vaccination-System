import tkinter as tk
import tkcalendar as tkc
import datetime
import User
import Patient
import Alerts
import Campus
import Appointment
from DataBaseConnection import DataBase 
import matplotlib.pyplot as plt

class LogInMenu:
    def __init__(self, user):
        self.currentUser = user
        self.email = ""
        self.password = ""
        self.successFlag = 0

    def mainWindow(self):
        # main login window
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.root.title('CVIS Log-In')

        emailLabel = tk.Label(self.root, text="Email").grid(row=0, column=0)
        self.email = tk.StringVar()
        emailEntry = tk.Entry(self.root, textvariable=self.email).grid(row=0, column=1)

        passwordLabel = tk.Label(self.root, text="Password").grid(row=1, column=0)
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(self.root, textvariable=self.password, show='*').grid(row=1, column=1)

        loginButton = tk.Button(self.root, text="Login", command=lambda:[self.root.destroy(), self.currentUser.checkLogIn(self.email.get(), self.password.get()), self.checkFlag()]).grid(row=4, column=1)

        self.root.mainloop() 

    def logInErrorWindow(self):
        # display if login is invalid 
        self.root = tk.Tk()
        self.root.geometry('200x100')
        label = tk.Label(self.root, text="Invalid Login")
        accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.mainWindow()])
        label.pack()
        accept.pack()
        self.root.mainloop()

    def checkFlag(self):
        # check if the login flag is set in the user login function then set own flag otherwise send to invalid login page
        if self.currentUser.flag == 1: 
            self.successFlag = 1
        else:
            self.logInErrorWindow()


class PatientMenu:
    def __init__(self, patient):
        self.currentPatient = patient
        self.createAppointmentMenu = AppointmentMenu(self.currentPatient)
        self.cancelAppointmentMenu = ViewApptsMenu(self.currentPatient)
        self.visualizationMenu = visualizationMenu()

    def mainWindow(self):
        # give patient all options to use system
        self.root = tk.Tk()
        self.root.geometry('400x200')
        self.root.title("User Menu")

        button1 = tk.Button(self.root, text = "Create an appointment", width = 50, command=lambda:[self.root.destroy(), self.createAppointmentMenu.tooManySmurfsWindow()])
        button2 = tk.Button(self.root, text = "View Existing Appointments", width = 50, command=lambda:[self.root.destroy(), self.cancelAppointmentMenu.notEnoughSmurfsWindow()])
        button3 = tk.Button(self.root, text = "Show Vaccination Data", width = 50, command = lambda:[self.visualizationMenu.vaccinationBarGraph()])
        button4 = tk.Button(self.root, text = "Show Campus Revenue", width = 50, command = lambda:[self.visualizationMenu.revenueGraph()])

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()



        self.root.mainloop()

class AppointmentMenu:

    def __init__(self, patient):
        self.currentPatient = patient
        self.tempAppt = Appointment.Appointment()
        self.selection = ""

    def tooManySmurfsWindow(self):
        # displays error if user has too many appointments
        if self.currentPatient.isEligible() == False:
            self.root = tk.Tk()
            self.root.geometry('400x100')
            label = tk.Label(self.root, text="Current User has too many scheduled appointments")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy()])
            label.pack()
            accept.pack()
            self.root.mainloop()
        else: 
            self.NameAndInsurance()

    def NameAndInsurance(self):
        # gives user options to input name and a radio button for if they have insurance or not and save results to current user
        self.root = tk.Tk()
        self.root.geometry('300x150')
        
        insurance = tk.IntVar()
        nameLabel = tk.Label(self.root, text="Name").grid(row = 0, column = 0)
        self.selection = tk.StringVar()

        nameEntry = tk.Entry(self.root, textvariable = self.selection).grid(row=0, column = 1)
        insuranceLabel = tk.Label(self.root, text="Do you have insurance?").grid(row=2, column=1)
        yesButton = tk.Radiobutton(self.root, text="Yes", variable = insurance, value=1).grid(row=3, column=1)
        noButton = tk.Radiobutton(self.root, text="No", variable = insurance, value = 0).grid(row=4, column=1)
        goButton = tk.Button(self.root, text="GO", command=lambda:[self.root.destroy(), self.currentPatient.setName(self.selection.get()), self.currentPatient.setInsurance(insurance.get()),self.tempAppt.setUserID(self.currentPatient.getID()), self.campusSelect()]).grid(row = 5, column = 1)
        
        self.root.mainloop()

    def campusSelect(self):
        # gives user option to select a campus from dropdown, upon confirmation save selection to temp Appointment
        campusNames = ["East Liverpool", "Geauga", "Kent", "Salem", "Stark", "Trumbull", "Tuscarawas"]
        self.root = tk.Tk()
        self.root.title("Select Campus")
        self.root.geometry('400x150')

        label = tk.Label(self.root, text="Select a Campus from the Dropdown Menu", width = 50)
        self.selection = tk.StringVar()
        self.selection.set(campusNames[0])
        Dropdown = tk.OptionMenu(self.root, self.selection, *campusNames)
        goButton = tk.Button(self.root, text="GO", width = 10, command=lambda:[self.root.destroy(),self.tempAppt.setCampus(self.selection.get()), self.dateSelect(self.selection.get())])

        label.pack()
        Dropdown.pack()
        goButton.pack()

        self.root.mainloop()
    
    def dateSelect(self, campus):
        #displays a calendar to allow user to pick a date, then checks if its valid
        currentDay = datetime.datetime.now().day
        currentMonth = datetime.datetime.now().month
        currentYear = datetime.datetime.now().year
        self.root = tk.Tk()
        self.root.title('Appointment Date Selection')
        self.root.geometry('600x600')

        dates = tkc.Calendar(self.root, selectmode="day", year=currentYear, month=currentMonth, day=currentDay)

        goButton = tk.Button(self.root, text = "GO", width = 20, command=lambda:[self.root.destroy(), self.dateErrorWindow(campus, dates.selection_get())])
        backButton = tk.Button(self.root, text = "Back", width = 20, command=lambda:[self.root.destroy(), self.campusSelect()])

        dates.pack(fill = "both", expand = "true")
        backButton.pack(side = tk.LEFT, pady = 15, padx = 20)      
        goButton.pack(side = tk.RIGHT, pady = 15, padx = 20)

        self.root.mainloop()
    
    def dateErrorWindow(self, campus, date):
        #check if date chosen is valid, if no display error window, if yes, save date in temp appt and display time menu
        if self.tempAppt.validDate(date) == False:
            self.root = tk.Tk()
            self.root.geometry('400x100')
            label = tk.Label(self.root, text="Pick a day between Monday & Friday and No more than 2 weeks in advance")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.dateSelect(self.tempAppt.campus.name)])
            label.pack()
            accept.pack()
            self.root.mainloop()
        else:
            self.tempAppt.setDate(date)
            self.timeSelect(campus, date)

    def timeSelect(self, campus, date):
        # give user a dropdown of available times for selected date
        availableTimes = self.tempAppt.getAvailableTimes()
        self.root = tk.Tk()
        self.root.geometry('400x150')
        self.root.title('Time Selection')
        self.selection = tk.StringVar()
        self.selection.set(availableTimes[0])
        label = tk.Label(self.root, text="Select an available time from the Dropdown", width = 50)
        goButton = tk.Button(self.root, text = "GO", command=lambda:[self.root.destroy(), self.tempAppt.setTime(self.selection.get()), self.confirmationWindow()])
        backButton = tk.Button(self.root, text="Back", command=lambda:[self.root.destroy(), self.dateSelectMenu(campus)])
        Dropdown = tk.OptionMenu(self.root, self.selection, *availableTimes)
        label.pack()
        Dropdown.pack()
        goButton.pack()
        backButton.pack()

    def confirmationWindow(self):
        #final confirmation to create appointment
        self.root = tk.Tk()
        self.root.geometry('200x100')
        label = tk.Label(self.root, text="Appointment Created", width = 50)
        accept = tk.Button(self.root, text= "OK", command=lambda:[self.root.destroy(), self.update()])
        label.pack()
        accept.pack()


    def update(self):
        #logs appointment, patient, & campus data to database, increase campus vaccines given, decrease campus vaccines on hand & creates follow up appointment
        self.currentPatient.insertAppointment(self.tempAppt)
        self.tempAppt.vaccine.setCurrentBrand(self.tempAppt.campus.currentBrand)
        self.tempAppt.createAppointment()
        self.tempAppt.campus.bookVaccine()
        
        if self.tempAppt.followUpSchedule() == True:
            self.currentPatient.insertAppointment(self.tempAppt)
            
        self.tempAppt.campus.updateVaccineInfo()
        self.currentPatient.logData()

        

class ViewApptsMenu:
    def __init__(self, patient):
        self.currentPatient = patient
        self.selection = ""

    def notEnoughSmurfsWindow(self):
        #display if user has no appointments scheduled
        if self.currentPatient.numberOfAppointments() == 0:
            self.root = tk.Tk()
            self.root.geometry('400x100')
            label = tk.Label(self.root, text="Current User has no scheduled appointments")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy()])
            label.pack()
            accept.pack()
            self.root.mainloop()
        else: 
            self.viewAppointmentsWindow()

    def viewAppointmentsWindow(self):
        # show appointments for current user and lets them select from dropdown menu, identified by an int 1 or 2 
        self.root = tk.Tk()
        self.root.title("Select Appointment")
        self.root.geometry('400x150')

        apptNum = []
        for i in range(len(self.currentPatient.appointments)):
            apptNum.append(i + 1)

        self.selection = tk.IntVar()
        self.selection.set(apptNum[0])

        label = tk.Label(self.root, text = "Select an Appointment")
        dropdown = tk.OptionMenu(self.root, self.selection, *apptNum)
        Cancel = tk.Button(self.root, text = "Cancel Appointment", command = lambda:[self.root.destroy(), self.cancellationWindow(self.selection.get() - 1)])
        Reschedule = tk.Button(self.root, text = "Reschedule Appointment", command = lambda:[self.root.destroy(), self.rescheduleWindow(self.selection.get() - 1)])

        label.pack()
        dropdown.pack()
        Cancel.pack()
        Reschedule.pack()

    def cancellationWindow(self, number):
        # show cancellation confirmation window and cancels appointment upon click of button
        self.root = tk.Tk()
        self.root.geometry('200x100')
        label = tk.Label(self.root, text="Appointment Canceled", width = 50)
        accept = tk.Button(self.root, text= "OK", command=lambda:[self.root.destroy(), self.cancel(number)])
        label.pack()
        accept.pack()

    def cancel(self, number):
        #delete appointment and change values in database
        tempAppt = Appointment.Appointment()
        tempAppt = self.currentPatient.appointments[number]
        del self.currentPatient.appointments[number]
        tempAppt.campus.unBookVaccine()
        tempAppt.campus.updateVaccineInfo()
        tempAppt.cancelAppointment()
        
    def rescheduleWindow(self, number):
        #cancel appointment and sends user back to original appointment scheduling window
        self.cancel(number)
        menu = AppointmentMenu(self.currentPatient)
        menu.NameAndInsurance()

        

class visualizationMenu:

    def __init__(self):
        self.campusNames = ["East Liverpool", "Geauga", "Kent", "Salem", "Stark", "Trumbull", "Tuscarawas"]
        self.campusData = []
        for i in self.campusNames:
            self.campusData.append(Campus.Campus(i))


    def vaccinationBarGraph(self):
        # display a bar graph of students vaccinated at each campus
        studentsVaccinatedList = []

        for i in self.campusData:
            studentsVaccinatedList.append(i.vaccinesGiven)

        plt.bar(self.campusNames, studentsVaccinatedList)
        plt.title('Students Vaccinated at each campus')
        plt.xlabel('Campus')
        plt.ylabel('StudentsVaccinated')
        plt.show()

    def revenueGraph(self):
        # display a graph of revenue from each campus
        revenueList = []
        for i in self.campusData:
            i.computeRevenue()
            revenueList.append(i.revenue)
        
        plt.bar(self.campusNames, revenueList)
        plt.title('Revenue Generated by Each Campus')
        plt.xlabel('Campus')
        plt.ylabel('Revenue Generated(Dollars)')
        plt.show()
            


        





        
        











    
    

