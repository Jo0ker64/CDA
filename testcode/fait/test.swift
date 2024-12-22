import Foundation

class Circle {
    var radius: Double

    init(radius: Double) {
        self.radius = radius
    }

    func area() -> Double {
        return Double.pi * pow(radius, 2)
    }

    func perimeter() -> Double {
        return 2 * Double.pi * radius
    }
}

func main() {
    let circle = Circle(radius: 5)
    print("Area: \(circle.area())")
    print("Perimeter: \(circle.perimeter())")
}

main()
