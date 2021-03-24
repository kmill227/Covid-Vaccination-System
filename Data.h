#ifndef DATA_H
#define DATA_H
#include "Campus.h"
class Data 
{
    public: 
        void visualizeData(); 
        int totalStudentsVaccinated();
        int revenueGenerated(); 
    private:
        Campus campuses[8];


};
#endif