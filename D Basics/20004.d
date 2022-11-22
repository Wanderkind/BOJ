import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

void main(){
    
    int n;
    readf!"%d"(n);

    foreach(i; 1..n+1){
        if([1, 2, 4, 5, 9, 14, 29].canFind(i)){
            writeln(i);
        }
    }
}
