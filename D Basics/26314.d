import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


char[] word(){

    char[21] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..21){
        if (s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

void sol(){

    char[] s = word();
    writeln(s);
    int v = 0, c = 0;

    foreach(i; s){

        if(['a', 'e', 'i', 'o', 'u'].canFind(i)){
            v++;
        }
        else{
            c++;
        }
    }

    writeln(v > c ? 1 : 0);
}

void main(){

    int n;
    scanf("%d", &n);

    while(n--){
        sol();
    }
}
