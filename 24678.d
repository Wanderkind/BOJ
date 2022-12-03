import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


void sol(){
    
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);

    int k = x%2 + y%2 + z%2;
    writeln(k>1 ? "B" : "R");
}

void main(){
    
    int t;
    scanf("%d", &t);

    while(t--){
       sol();
    }
}
