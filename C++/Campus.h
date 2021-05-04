#ifndef CAMPUS_H
#define CAMPUS_H

/************************
 * Class definition : Campus
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Campus {

	public:

		int studentsVaccinated();
		int moneyGenerated();
		void setCampus();
		bool isRegional(); 
	private:
		int vaccinations; 
		int revenue; 
		int id; 
};


#endif
