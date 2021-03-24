#ifndef PATIENT_H
#define PATIENT_H
class Patient
{
    public: 
        Insurance getInsurance(); 
        Appointment scheduledAppointment(); 
        Vaccine vaccineInfo(); 
        bool courseCompleted(); 
    private:
};
#endif