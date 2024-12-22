use std::f64::consts::PI;

struct Circle {
    radius: f64,
}

impl Circle {
    fn new(radius: f64) -> Self {
        Circle { radius }
    }

    fn area(&self) -> f64 {
        PI * self.radius.powi(2)
    }

    fn perimeter(&self) -> f64 {
        2.0 * PI * self.radius
    }
}

fn main() {
    let circle = Circle::new(5.0);
    println!("Area: {:.2}", circle.area());
    println!("Perimeter: {:.2}", circle.perimeter());
}
