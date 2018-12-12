// Return sum of two numbers 
object Solution {
  def main(args: Array[String]) {
    
    val number_1 = io.StdIn.readInt()
    val number_2 = io.StdIn.readInt()
    val sum = sumOfNumbers(number_1, number_2)
    println (sum)

  }

  def sumOfNumbers (number_1:Int, number_2:Int) : Int = {
    return number_1 + number_2
  }
}