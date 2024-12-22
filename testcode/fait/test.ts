// TypeScript Example
class Circle {
    radius: number;

    constructor(radius: number) {
        this.radius = radius;
    }

    area(): number {
        return Math.PI * this.radius ** 2;
    }

    perimeter(): number {
        return 2 * Math.PI * this.radius;
    }
}

function main(): void {
    const circle = new Circle(5);
    console.log(`Area: ${circle.area()}`);
    console.log(`Perimeter: ${circle.perimeter()}`);
}

main();
