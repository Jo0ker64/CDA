# Ruby Example
class Circle
    def initialize(radius)
        @radius = radius
    end

    def area
        Math::PI * @radius**2
    end

    def perimeter
        2 * Math::PI * @radius
    end
end

def main
    circle = Circle.new(5)
    puts "Area: #{circle.area}"
    puts "Perimeter: #{circle.perimeter}"
end

main
