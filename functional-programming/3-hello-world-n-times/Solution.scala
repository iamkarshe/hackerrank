object Solution extends App{

  var n = scala.io.StdIn.readInt
  f(n)

  def f(n:Int) = {
    for (i <- 1 to n){
      println ("Hello World")
    }
  }

}