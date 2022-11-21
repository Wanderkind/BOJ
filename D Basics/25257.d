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
    
    double d,s,e;
    readf!"%f %f %f"(d,s,e);

    double ans = (s*(d-s)-e*max(0,2*s+e-d))/d/(d-s-e);
    printf("%.9f",ans);
}
