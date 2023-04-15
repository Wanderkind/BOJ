import java.util.Scanner


fun main(){
    val sc = Scanner(System.`in`)

    val n = sc.nextInt()
    val m = sc.nextInt()

    val k = minOf(n, m) - 1
    val x = k/2
    val y = x + k%2

    if(k%2 == 1){
        print("%d %d".format(x, y))
    }
    else{
        val z = y + maxOf(n, m) - 1 - k
        if(n < m){
            print("%d %d".format(y, z))
        }
        else{
            print("%d %d".format(z, y))
        }
    }
}
