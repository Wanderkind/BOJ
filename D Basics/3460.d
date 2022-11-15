import std.stdio;
//import std.algorithm;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

void sol(){
    
    int n;
    scanf("%d",&n);

    int i = 0;
    while(n){
        i++;
        if(n%2){
            printf("%d ",i-1);
        }
        n >>= 1;
    }
    printf("\n");
}

void main(){
    
    int n;
    readf!"%d"(n);
    while(n--){
        sol();
    }
}
