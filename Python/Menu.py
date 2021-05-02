import tkinter as tk
from functools import partial
import tkcalendar as tkc
import datetime
import User
import Admin
import Patient
import Alerts
import Campus
from DatabaseConnection import DataBase 

class Menu:
    def __init__(self):
        self.currentUser = User.User()
        self.campusNames = ["East Liverpool", "Geauga", "Kent", "Salem", "Stark", "Trumbull", "Tuscarawas"]



    def logInMenu(self):
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.root.title('CVIS Log-In')

        emailLabel = tk.Label(self.root, text="Email").grid(row=0, column=0)
        self.currentUser.email = tk.StringVar()
        emailEntry = tk.Entry(self.root, textvariable=self.currentUser.email).grid(row=0, column=1)

        passwordLabel = tk.Label(self.root, text="Password").grid(row=1, column=0)
        self.currentUser.password = tk.StringVar()
        passwordEntry = tk.Entry(self.root, textvariable=self.currentUser.password, show='*').grid(row=1, column=1)

        logIn = partial(self.currentUser.checkLogIn, self.root)

        loginButton = tk.Button(self.root, text="Login", command=logIn).grid(row=4, column=1)

        self.root.mainloop() 

        if self.currentUser.flag == 1:
            if self.currentUser.isAdmin == 1: 
                self.currentUser = Admin.Admin()
                adminMenu()
            else: 
                self.currentUser = Patient.Patient()
                self.patientMenu()
        elif self.currentUser.flag == 0: 
            self.root = tk.Tk()
            self.root.geometry('200x100')
            label = tk.Label(self.root, text="Invalid Login")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.logInMenu()])
            label.pack()
            accept.pack()
            self.root.mainloop()

    def adminMenu(self):
        self.root = tk.Tk()
        self.root.title("Administrator Menu")
        self.root.geometry('400x100')

        button1 = tk.Button(self.root, text = "Register a new User", width = 50, command=self.currentUser.registerUser)
        button2 = tk.Button(self.root, text = "Display Booked Appointments", width = 50, command=self.currentUser.displayAllAppointments)
        button3 = tk.Button(self.root, text = "Log a Given Vaccine", width = 50, command=self.currentUser.logVaccine)

        button1.pack()
        button2.pack()
        button3.pack()

        self.root.mainloop()

    def patientMenu(self): 
        self.root = tk.Tk()
        self.root.geometry('400x100')
        self.root.title("User Menu")

        button1 = tk.Button(self.root, text = "Create an appointment", width = 50, command=lambda:[self.root.destroy(), self.campusSelectMenu()])
        button2 = tk.Button(self.root, text = "Cancel an Appointment", width = 50, command=self.cancelAppointmentMenu)
        button3 = tk.Button(self.root, text = "Reschedule an Appointment", width = 50, command=self.rescheduleAppointmentMenu)

        button1.pack()
        button2.pack()
        button3.pack()

        self.root.mainloop()

    def campusSelectMenu(self):
        self.root = tk.Tk()
        self.root.title("Select Campus")
        self.root.geometry('400x150')

        label = tk.Label(self.root, text="Select a Campus from the Dropdown Menu", width = 50)
        selection = tk.StringVar()
        selection.set(self.campusNames[0])
        Dropdown = tk.OptionMenu(self.root, selection, *self.campusNames)
        goButton = tk.Button(self.root, text="GO", width = 10, command=lambda:[self.root.destroy(),self.dateSelectMenu(selection.get())])
        backButton = tk.Button(self.root, text="Back", width = 10, command=lambda:[self.root.destroy(), self.patientMenu()])

        label.pack()
        Dropdown.pack()
        goButton.pack()
        backButton.pack()

        self.root.mainloop()

    def dateSelectMenu(self, campus):
        
        self.root = tk.Tk()
        self.root.title('Appointment Date Selection')
        self.root.geometry('600x600')

        dates = tkc.Calendar(self.root, selectmode="day", year=2021, month=5, day=1)
        goButton = tk.Button(self.root, text = "GO", width = 20, command=lambda:[self.root.destroy(), self.timeSelectMenu(campus, dates.selection_get())])
        backButton = tk.Button(self.root, text = "Back", width = 20, command=lambda:[self.root.destroy(), self.campusSelectMenu()])
        dates.pack(fill = "both", expand = "true")

        backButton.pack(side = tk.LEFT, pady = 15, padx = 20)      
        goButton.pack(side = tk.RIGHT, pady = 15, padx = 20)


        self.root.mainloop()


    def timeSelectMenu(self, campus, date):
        if date.weekday() > 4:
            self.root = tk.Tk()
            self.root.geometry('200x100')
            label = tk.Label(self.root, text="Pick a day between Monday & Friday")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.dateSelectMenu(campus)])
            label.pack()
            accept.pack()
            self.root.mainloop()

        db = Database()
        sql = "SELECT AppointmentTime FROM appointment WHERE AppointmentDate=%s AND Campus =%s"
        args = (date, campus)
        db.cursor.execute(sql, args)
        bookedAppts = db.cursor.fetchall()

        validAppointments = []
        hours = 8
        minutes = 0
        seconds = 0

        for i in range(10):
            hours += 1
            minutes = 0
        for i in range(6):
            validAppointments.append(datetime.time(hours, minutes, seconds))
            minutes += 10

        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.title('Time Selection')



        


                
        




    def cancelAppointmentMenu(self): 
        pass

    def rescheduleAppointmentMenu(self):
        pass

    
menu = Menu()
menu.logInMenu()
