import std.stdio;
import std.algorithm.mutation;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

void main(){
    
    long a,b,t;
    readf!"%d %d"(a,b);
    if(a>b){
        swap(a,b);
    }
    long k = b-a+-1;
    writeln(k>0?k:0);
    foreach(i;1..b-a){
        t = a+i;
        printf("%lld ",t);
    }
}
