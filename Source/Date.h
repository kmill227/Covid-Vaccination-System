#ifndef DATE_H
#define DATE_H

/************************
 * Class definition : Date
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Date
{
    public: 
        void setDate(int mm, int dd, int yyyy);
        int getMonth(); 
        int getDay(); 
        int getYear(); 
    private: 
        int month, day, year; 
};
#endif