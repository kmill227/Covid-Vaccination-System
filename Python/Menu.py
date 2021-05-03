import tkinter as tk
from functools import partial
import tkcalendar as tkc
import datetime
import User
import Admin
import Patient
import Alerts
import Campus
import Appointment
from DataBaseConnection import DataBase 



class LogInMenu:
    def __init__(self, user):
        self.currentUser = user
        self.email = ""
        self.password = ""
        self.successFlag = 0

    def mainWindow(self):
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
        self.root = tk.Tk()
        self.root.geometry('200x100')
        label = tk.Label(self.root, text="Invalid Login")
        accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.mainWindow()])
        label.pack()
        accept.pack()
        self.root.mainloop()

    def checkFlag(self):
        if self.currentUser.flag == 1: 
            self.successFlag = 1
        else:
            self.logInErrorWindow()


class PatientMenu:
    def __init__(self, patient):
        self.currentPatient = patient
        self.createAppointmentMenu = AppointmentMenu(self.currentPatient)
        self.cancelAppointmentMenu = ViewApptsMenu(self.currentPatient)

    def mainWindow(self):
        self.root = tk.Tk()
        self.root.geometry('400x100')
        self.root.title("User Menu")

        button1 = tk.Button(self.root, text = "Create an appointment", width = 50, command=lambda:[self.root.destroy(), self.createAppointmentMenu.tooManySmurfsWindow()])
        button2 = tk.Button(self.root, text = "Cancel an Appointment", width = 50, command=lambda:[self.root.destroy(), self.cancelAppointmentMenu.notEnoughSmurfsWindow()])
        #button3 = tk.Button(self.root, text = "Reschedule an Appointment", width = 50, command=self.rescheduleAppointmentMenu)
        #button4 = tk.Button(self.root, text = "View my appointments", width = 50, command=self.viewAppointmentsMenu)

        button1.pack()
        button2.pack()
        #button3.pack()
        #button4.pack()

        self.root.mainloop()

class AppointmentMenu:

    def __init__(self, patient):
        self.currentPatient = patient
        self.tempAppt = Appointment.Appointment()
        self.selection = ""

    def tooManySmurfsWindow(self):
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

        if self.tempAppt.validDate(date) == False:
            self.root = tk.Tk()
            self.root.geometry('200x100')
            label = tk.Label(self.root, text="Pick a day between Monday & Friday and No more than 2 weeks in advance")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.dateSelectMenu(self.tempAppt.campus.name)])
            label.pack()
            accept.pack()
            self.root.mainloop()
        else:
            self.tempAppt.setDate(date)
            self.timeSelect(campus, date)

    def timeSelect(self, campus, date):
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
        self.root = tk.Tk()
        self.root.geometry('200x100')
        label = tk.Label(self.root, text="Appointment Created", width = 50)
        accept = tk.Button(self.root, text= "OK", command=lambda:[self.root.destroy(), self.update()])
        label.pack()
        accept.pack()


    def update(self):
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
        if self.currentPatient.numberofAppointments() == 0:
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
        self.root = tk.Tk()
        self.root.title("Select Appointment")
        self.root.geometry('400x150')


        
        











    
    

