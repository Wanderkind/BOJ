import java.util.Scanner
import kotlin.math.*

fun main(){
    val sc = Scanner(System.`in`)

    val n = readLine()?.toInt()!!
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = sc.nextInt()
    }
    arr.sort()
    val s = arr.sum().toDouble()

    if(n == 1){
        print(arr[0])
    }
    else if(n == 2){
        print(s/2)
    }
    else{
        print(max(arr[n-2].toDouble(), s/n))
    }
}
