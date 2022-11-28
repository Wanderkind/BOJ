import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


void sol(){

    int x, y, c, a, k;
    scanf("%d %d\n%d %d", &x, &y, &c, &a);
    c--;
    while(c--){
        
        scanf("%d", &k);
        a = gcd(a, k);
    }

    writeln(abs(x)%a + abs(y)%a ? "Gave up" : "Ta-da");
}

void main(){
    
    int t;
    scanf("%d", &t);
    while(t--){
        sol();
    }
}
