import java.util.Scanner

fun main(){
    val sc = Scanner(System.`in`)

    val x = readLine()?.toInt()!!
    val n = readLine()?.toInt()!!
    var s = x*(n+1)

    for (i in 0 until n) {
        val k = sc.nextInt()
        s -= k
    }

    print(s)
}
