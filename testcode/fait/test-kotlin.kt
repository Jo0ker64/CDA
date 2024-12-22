import kotlin.math.PI
import kotlin.math.pow

class Circle(private val radius: Double) {

    fun area(): Double {
        return PI * radius.pow(2)
    }

    fun perimeter(): Double {
        return 2 * PI * radius
    }
}

fun main() {
    val circle = Circle(5.0)
    println("Area: %.2f".format(circle.area()))
    println("Perimeter: %.2f".format(circle.perimeter()))
}
