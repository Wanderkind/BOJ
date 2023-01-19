import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    val arr = IntArray(4)
    for (i in 0 until 4) {
        arr[i] = sc.nextInt()
    }
    sc.close()

    arr.sort()
    println(arr[0]*arr[1] + arr[2]*arr[3])
}
