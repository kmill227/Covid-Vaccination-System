#ifndef DATA_H
#define DATA_H
#include "Campus.h"

/************************
 * Class definition : Data
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

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