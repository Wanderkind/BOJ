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

    int n, a, b, d, ans = 0;
    scanf("%d", &n);
    while(n--){
        scanf("%c%c%d", &a, &b, &d);
        ans += (-d<=90);
    }

    writeln(ans);
}

void main(){
    
    sol();
}
