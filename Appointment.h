#ifndef APPOINTMENT_H
#define APPOINTMENT_H
#include "Date.h"
#include "Doctor.h"
class Appointment
{
    public: 
        void createAppointment(Date date, Doctor dr); 
        Date getScheduledAppointment(); 
        Doctor getDoctor(); 
        Station getStation(); 
    private: 


};
#endif