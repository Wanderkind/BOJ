fun main() {
    val n = readLine()?.toInt()
    for(i in 0 until n!!){
        for(j in 1 until n-i){
            print(" ")
        }
        for(j in 0 until i){
            print("* ")
        }
        print("*\n")
    }
}
