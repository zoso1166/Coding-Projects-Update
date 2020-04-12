# include <iostream>
using namespace std;

int main()
{
int legnth, width, area; // Declares variables and their values

cout << "Enter the legnth of the triangle: ", cin >> legnth;
cout << "Enter the width of the triangle: ", cin >> width;

area = legnth * width;   // calculation of area

cout << "The area is ";          // displays results for calculations
cout << area;

return 0;
}