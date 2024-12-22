// C++ Example
#include <iostream>
#include <cmath>
using namespace std;

class Circle {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}

    double area() {
        return M_PI * radius * radius;
    }

    double perimeter() {
        return 2 * M_PI * radius;
    }
};

int main() {
    Circle circle(5);
    cout << "Area: " << circle.area() << endl;
    cout << "Perimeter: " << circle.perimeter() << endl;
    return 0;
}
