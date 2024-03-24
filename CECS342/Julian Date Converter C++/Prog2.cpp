//Saiah Montoya
//CECS 342-07
//Prog 2- Overload Operators C++
// Due Date (10/3/2023)
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
using namespace std;

int g2j( int m, int d, int y)
{
    
    int JD;
    int I = y, J = m, K = d;
    
    JD= K-32075+1461*(I+4800+(J-14)/12)/4+367*(J-2-(J-14)/12*12)/12-3*((I+4900+(J-14)/12)/100)/4;
    
    
    return JD;
}

class Date
{
    private:
        //create private data members
        int month, day, year;
        int * dptr;
        static int tcount;

    public:
        //public data members
        Date()
        {
            //default constructor with pointers and count of temporary objects
            dptr = new int[3];
            dptr[0] = 1;
            dptr[1] = 1;
            dptr[2] = 1970;
            tcount+=1;
        };

        Date(int m, int d, int y)
        {
            //overloaded constructor with pointers to month day and year
            dptr = new int[3];
            dptr[0] = m;
            dptr[1] = d;
            dptr[2] = y;
            tcount++;
        };
        
        Date(const Date& d)
        {
            //copy constructor saves object to memory
            dptr = new int[3];
            dptr[0] = d.dptr[0];
            dptr[1] = d.dptr[1];
            dptr[2] = d.dptr[2];
            tcount += 1;
        };
        
        Date(int jd)
        {
            //overload constructor, date -> julian
            j2g(jd);
            tcount += 1;
        };

        ~Date()
        {
            //destructor, deallocates memory
            delete[] dptr;
            tcount-= 1;
        };

    	static int count()
    	{
    	    //track object temp count
			return tcount;
		};

        void display()
        {
            //outputs to terminal
            cout << month << '/' << day << '/' << year << endl;
        };

    	int operator=(Date d)
    	{
  			//assign int value to day
  		    dptr[0] = d.dptr[0];
  		    dptr[1] = d.dptr[1];
  		    dptr[2] = d.dptr[2];
  		    return 0;
    	};

        int operator-(Date d)
        {
            //int - d1
            int x = julian();
            int y = d.julian();
            
            int z = x - y;
            return z;
        };

    	Date operator-(int n)
    	{
    	    // d1 - int
      		int x = julian();
      		x -= n;
     
 			*this = j2g(x);
 			return *this;
    	};

        Date operator+(int n)
    	{
    	    //D1 + int
  			int x = julian();
      		x += n;
      		return j2g(x);
    	};

       friend Date operator+(int n, const Date &d)
        {
            // Int + D1
            int x = d.julian();
            x += n;
            return Date::j2g(x);
        };

        bool operator>(Date d) const
        {
            //return True if D1 > D2 by comparing the values at month day and year
            if (dptr[0] > d.dptr[0]) 
            {
                return true;
            }
            if (dptr[0] < d.dptr[0]) 
            {
                return false;
            }
            if (dptr[2] > d.dptr[2]) 
            {
                return true;
            }
            if (dptr[2] < d.dptr[2]) 
            {
                return false;
            }
            return dptr[1] > d.dptr[1];
        };

        bool operator<(Date d)
        {
            //return True if D1 < D2 by comparing values in month day and year
            if (dptr[0] < d.dptr[0]) 
            {
                return true;
            }
            if (dptr[0] > d.dptr[0]) 
            {
                return false;
            }
            if (dptr[2] < d.dptr[2]) 
            {
                return true;
            }
            if (dptr[2] > d.dptr[2]) 
            {
                return false;
            }
            return dptr[1] < d.dptr[1];
        };

    	bool operator==(Date& d)
    	{
    	    //return True if D1 and D2 are Equal
            return (this->year == d.year) && (this->month == d.month) && (this->day == d.day);
		};

        Date operator++(int)
        {
            //D1++ operator
            int x = julian();
            x += 1;
            *this = j2g(x);
            Date d = *this;
            return d;
        };

        Date operator++()
        {
            //++D1 operator
            int x = julian();
            x += 1;
            *this = Date::j2g(x);
            return *this;
        };

    	Date operator--()
    	{
    	    //--D1 operator
            int x = julian();
            x -= 1;
            *this = j2g(x);
            return *this;
		};

        Date operator--(int)
    	{
    	    //D1-- operator
            Date temp = *this;
		    int x = julian();
		    x -= 1;
		    *this = j2g(x);
		    return temp;
    	};
    	
    	Date operator-=(int n)
    	{
    	    // D1 -= int
    	    int x = julian();
    	    x -= n;
    	    *this = j2g(x);
    	    return *this;
    	    //return stored value
    	};
        
        Date operator+=(int n)
        {
            // D1 += int 
            int x = julian();
            x += n;
            *this = j2g(x);
            return *this;
            //return stored value
        };

        int julian() const //date to julian date
        {
            return g2j(dptr[0], dptr[1], dptr[2]);
        };

        int getMonth() // return month as int
        {
            return dptr[0];
        };

        int getDay() //return Day as int
        {
            return dptr[1];
        };
        
        int getYear() //return year as int
        {
            return dptr[2];
        };
        
        static Date j2g(int jd)
        {
            //Julian date to Gregorian
            Date date;
            int I, J, K;

            //Equation
            int L = jd + 68569;
            int N = 4 * L / 146097;
            L = L - (146097 * N + 3) / 4;
            I = 4000 * (L + 1) / 1461001;
            L = L - 1461 * I / 4 + 31;
            J = 80 * L / 2447;
            K = L - 2447 * J / 80;
            L = J / 11;
            J = J + 2 - 12 * L;
            I = 100 * (N - 49) + I + L;
            
            //Store to memory
            date.dptr[2] = I;  //Year
            date.dptr[1] = K;  //Day
            date.dptr[0] = J;  //Month
            return date;
        };

        // string getMonthName() //return name of month, 3 letters abr.
        // {
        //     const char* monthNames[] = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
        //     return monthNames[month - 1]; 
        // }
        
        // string getDayName() //return week day name
        // {
        //     int m = month;
        //     int d = day;
        //     int y = year;

        //     if (m < 3)
        //     {
        //         m += 12;
        //         y--;
        //     }

        //     int k = y % 100;
        //     int j = y / 100;

        //     int dayOfWeek = (d + (13 * (m + 1)) / 5 + k + (k / 4) + (j / 4) - (2 * j)) % 7;

        //     const char* dayNames[] = { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
        //     return dayNames[dayOfWeek];
        // }
        
	    friend ostream& operator<<(std::ostream& os, Date d)
	    {
	        //Ostream (os) operator
		    os << d.getMonth() << "/" << d.getDay() << "/" << d.getYear();
		    return os;
	    };
};
//declare initial count
int Date::tcount = 0;

int main() 
{   
    Date epoch;
    Date duedate(10,3,2023);
    Date today(duedate);


	cout << endl;
	cout << "Today is " << today << endl;
	cout << "This program is due on " << duedate;
	cout << endl;
    Date dtemp(duedate);
    dtemp++;
	cout << "If you turn this assignment in on "<<dtemp<<" then is will be late.\n";
	cout << "It is due on "<<--dtemp<<" so don't be late.\n";
	cout << "One week from due date is "<<duedate+7<<endl;
    cout << "One week from due date is "<<7+duedate<<endl;
	cout << "One week earlier from due date is "<<duedate-7<<endl;

	cout << "The Unix Epoch date is "<<epoch<<" : ";
	cout << "The Epoch date was "<< duedate - epoch << " days ago\n";
	
	cout << "Today is Julian date "<<duedate.julian()<<endl;;
	cout << "Tomorrrow is Julian date "<<(++duedate).julian()<<endl;;

	cout << "The very first Julian date was " << Date(10,3,2023) - Date(10,3,2023).julian()<<endl;

	cout << "The very first Julian date was " << today - today.julian()<<endl;


	Date yesterday, tomorrow;
	yesterday = today-1;
	tomorrow = today+1;
	
	cout << "Yesterday was "<<yesterday << endl;
	cout << "Today is "<<today<<endl;
	cout << "Tomorrow is "<<tomorrow<<endl;

	cout << "Today is ";
	cout << ((today>tomorrow)?"greater than":"not greater than");
	cout << " than tomorrow\n";

	cout << "Today is ";
	cout << ((today<tomorrow)?"less than":"not less than");
	cout << " than tomorrow\n";

	cout << "Today is ";
	cout << ((today==tomorrow)?"equal to":"not equal to");
	cout << " tomorrow\n";

	getchar();
	return 0;
}	
