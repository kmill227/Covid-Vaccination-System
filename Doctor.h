#ifndef DOCTOR_H
#define DOCTOR_H
#include <string>
#include "Station.h"
class Doctor
{
    public: 
        int paySalary(); 
        void setStation(); 
        Station getStation(); 
        std::string getName();
    private: 
        std::string name; 
        int salary; 
        Station workingStation; 
};
#endif