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

int buzz(char[21] c){

    return [
        "he\0__________________",
        "she\0_________________",
        "him\0_________________",
        "her\0_________________"
    ].canFind(c);
}

void sol(){
    
    int words, shocks = 0;
    scanf("%d", &words);

    char[21] c = "_____________________";
    while(words--){
        scanf("%s", &c);
        shocks += buzz(c);
        c = "_____________________";
    }
    
    writeln(shocks);
}

void main(){

    sol();
}
