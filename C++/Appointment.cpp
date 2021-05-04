#include "Appointment.h"

void Appointment::createAppointment(Date date, Doctor doc, Station station)
{

}

Date Appointment::getScheduledAppointment()
{
    return appointmentDate;
}

Doctor Appointment::getDoctor()
{
    return dr;
}

Station Appointment::getStation()
{
    return vaccinationStation; 
}