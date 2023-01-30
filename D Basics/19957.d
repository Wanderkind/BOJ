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


void main(){
    
    char[2] s;
    scanf("%s", &s);

    int file = cast(int) s[0] - 96;
    int rank = cast(int) s[1] - 48;

    bool lrfilp = 4 < file;
    bool udfilp = 4 < rank;

    if(lrfilp){file = 9 - file;}
    if(udfilp){rank = 9 - rank;}

    int rf, rr, bf, br;

    if(file == 1 && rank == 4){rf = 8; rr = 4;}
    else{rf = 5; rr = rank;}
    if(file <= rank){bf = 8 - rank + file; br = 8;}
    else{bf = 8; br = 8 + rank - file;}

    if(lrfilp){rf = 9 - rf; bf = 9 - bf;}
    if(udfilp){rr = 9 - rr; br = 9 - br;}

    writeln(cast(char) (rf + 96), cast(char) (rr + 48));
    writeln(cast(char) (bf + 96), cast(char) (br + 48));
}
