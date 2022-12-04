import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


bool win(int a, int b){
	
    if(a+b == 0){
        return false;
    }

	if(a+b == 1){
        return true;
    }

    if(a>b){
        swap(a, b);
    }

    if(b<=2*a){
        int s = (a+b)%5;
        return [0, 1, 3].canFind(s);
    }

    if(a == 1 && b == 3){
        return true;
    }

    if(a%2){
        return true;
    }

    return b%2 == 1-(a%4)/2;
}

void sol(){
    
    int a, b;
    scanf("%d %d", &a, &b);

    writeln(win(a, b)? "Alice" : "Bob");
}

void main(){

    sol();
}
