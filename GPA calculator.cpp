#include <iostream>
#include <string>

using namespace std;

int main ()
{
    char choice;
    float gradepoint;
    float total_gradepoint = 0;
    int credit_hours;
    int total_credit_hours = 0;

    cout<<"Welcome to the CGPA calculator." <<endl;
    cout<<"NB:The various gradepoints are: A - 4.0; B+ - 3.5; B - 3.0; C+ - 2.5; C - 2.0; D+ - 1.5; D - 1.0; E - 0.5; F - 0.0\n"<<endl;

    do 
    {
        cout<<"Enter the gradepoint for a course and its corresponding credit hours" <<endl;
        cin>> gradepoint>> credit_hours;

        total_gradepoint += gradepoint * credit_hours;
        total_credit_hours += credit_hours;

        cout<<"Do you want to enter another set of results? (y/n) :"<<endl;
        cin>> choice;

    } while (choice == 'y' || choice == 'Y');

    float CGPA = total_gradepoint / total_credit_hours;
    cout<<"Your CGPA is " <<CGPA; 

    return 0;
}