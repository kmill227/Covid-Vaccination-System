import tkinter as tk
from functools import partial
import User
import Admin
import Patient
import Alerts
import Campus

class Menu:
    def __init__(self):
        self.currentUser = User.User()
        self.campusNames = ["East Liverpool", "Geauga", "Kent", "Salem", "Stark", "Trumbull", "Tuscarawas"]
        self.campusList = []
        for i in campusNames:
            campusList.append(campusNames[i])


    def LogInScreen(self):
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
                patientMenu()
        elif self.currentUser.flag == 0: 
            self.root = tk.Tk()
            self.root.geometry('200x100')
            label = tk.Label(self.root, text="Invalid Login")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.LogInScreen()])
            label.pack()
            accept.pack()
            self.root.mainloop()

    def adminMenu(self):
        self.root = tk.Tk()
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
        button1 = tk.Button(self.root, text = "Create an appointment", width = 50, command=self.campusSelectMenu)
        button2 = tk.Button(self.root, text = "Cancel an Appointment", width = 50, command=self.cancelAppointmentMenu)
        button3 = tk.Button(self.root, text = "Reschedule an Appointment", width = 50, command=self.rescheduleAppointmentMenu)
        button1.pack()
        button2.pack()
        button3.pack()
        self.root.mainloop()

    def campusSelectMenu(self):
        self.root = tk.Tk()
        self.root.geometry('400x100')
        label = tk.Label(self.root, text="Select a Campus from the Dropdown Menu", width = 50)
        selection = tk.StringVar()
        selection.set(self.campusNames[0])
        Dropdown = tk.OptionMenu(self.root, selection, *self.campusNames)
        button = tk.Button(self.root, text="GO", width = 10)
        label.pack()
        Dropdown.pack()
        button.pack()
        self.root.mainloop()

    def dateSelectMenu(self):
        pass

    def cancelAppointmentMenu(self): 
        pass

    def rescheduleAppointmentMenu(self):
        pass

    
menu = Menu()
menu.campusSelectMenu()
