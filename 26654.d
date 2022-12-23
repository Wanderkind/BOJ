import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


int sol(){
    
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);

    double r = sqrt(cast(double)2*a/n/sin(2*PI/n)); // 정다각형 외접원의 반지름
    double R = sqrt(cast(double)b/PI); // 원의 반지름

    if(r <= R){
        return n;
    }
    
    return cast(int)floor(asin(R/r)*n/PI)+1;
}

void main(){
    
    int t;
    scanf("%d", &t);

    while(t--){
        writeln(sol());
    }
}
