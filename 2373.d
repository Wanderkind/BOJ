import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

int sol(int n){
    
    int a = 0, b = 0, c = 1, s = 1;

    while(s < n){
        a = b;
        b = c;
        c = a+b;
        s += c;
    }

    int k = c-s+n-1;
    
    while(k && (k != b)){
        if(k < b){
            c = b;
            b = a;
            a = c-b;
        }
        else{
            k -= b;
            b -= a;
            a -= b;
            c = a+b;
        }
    }
    
    return k?b:-1;
}

void main(){
    
    int n;
    readf!"%d"(n);

    writeln(sol(n));
}
