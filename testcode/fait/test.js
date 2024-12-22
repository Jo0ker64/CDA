// JavaScript Example
class Circle {
    constructor(radius) {
        this.radius = radius;
    }

    area() {
        return Math.PI * this.radius ** 2;
    }

    perimeter() {
        return 2 * Math.PI * this.radius;
    }
}

function main() {
    const circle = new Circle(5);
    console.log(`Area: ${circle.area()}`);
    console.log(`Perimeter: ${circle.perimeter()}`);
}

main();
