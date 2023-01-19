fun main() {
    val n = readLine()?.toInt() // convert the string to an integer
    for(i in 1 until n!!){
        for(j in 0 until n-i){
            print(" ")
        }
        print("*")
        if(i > 1){
            for(j in 0 until 2*i-3){
                print(" ")
            }
            print("*")
        }
        println()
    }
    for(i in 1 until 2*n){
        print("*")
    }
}
