fun main(){
    val n = readLine()?.toInt()!!
    if(n % 400 == 0){
        print(1)
    }
    else if(n % 100 == 0){
        print(0)
    }
    else if(n % 4 == 0){
        print(1)
    }
    else{
        print(0)
    }
}
