import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


void sol(){

    long n, l, w, s = 0, S = 0;
    long[100000] x;
    scanf("%d %d", &n, &l);

    foreach(i; 0..n){scanf("%ld", &x[i]);}
    foreach(i; 0..n){scanf("%ld", &w); s += w; S += w*x[i];}
    
    printf("%.9lf", cast(double)S/s);
}

void main(){
    
    sol();
}
