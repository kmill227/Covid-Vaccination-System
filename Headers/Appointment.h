#ifndef APPOINTMENT_H
#define APPOINTMENT_H
#include "Date.h"
#include "Doctor.h"
#include "Station.h"

/************************
 * Class definition : Appointment
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Appointment
{
    public: 
        void createAppointment(Date date, Doctor doc, Station station); 
        Date getScheduledAppointment(); 
        Doctor getDoctor(); 
        Station getStation(); 
    private: 
        Date appointmentDate; 
        Doctor dr; 
        Station vaccinationStation; 


};
#endif