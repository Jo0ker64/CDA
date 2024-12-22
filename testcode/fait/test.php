<?php
// PHP Example
class Circle {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function area() {
        return pi() * $this->radius ** 2;
    }

    public function perimeter() {
        return 2 * pi() * $this->radius;
    }
}

function main() {
    $circle = new Circle(5);
    echo "Area: " . $circle->area() . PHP_EOL;
    echo "Perimeter: " . $circle->perimeter() . PHP_EOL;
}

main();
?>
