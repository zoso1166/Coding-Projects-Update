// Convert feet to meters by James Page April 12 2020 /

#include <iostream> 
using namespace std;

int main()
{
double f; // creates feet measurements
double m; // creates meter measurements

cout << "Enter the legnth in feet: ", cin >> f;
m = f / 3.28;

cout << f << " feet is equal to " << m << " meters.";

return 0;
}