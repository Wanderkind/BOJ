import java.util.Scanner

fun f(a: Int, b: Int): Int {
    if(a <= b){
        return b-a
    }
    else if(a%2 == 1){
        return 1+f(a+1, b)
    }
    else{
        return 1+f(a/2, b)
    }
}

fun main(){
    val sc = Scanner(System.`in`)

    val a = sc.nextInt()
    val b = sc.nextInt()

    print(f(a, b))
}
