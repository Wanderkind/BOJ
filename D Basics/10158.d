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
    
    int w, h, p, q, t;
    scanf("%d %d", &w, &h);
    scanf("%d %d", &p, &q);
    scanf("%d", &t);

    int x = p+t, y = q+t;
    int u = x%w, v = y%h;

    printf("%d %d", (x/w)%2 ? w-u : u, (y/h)%2 ? h-v : v);
}

void main(){
    
    sol();
}
