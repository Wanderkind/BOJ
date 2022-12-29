import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
import std.array;
//import std.bigint;
//import std.string;


char[] word(){

    char[31] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..31){
        if (s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

char[] latin(char[] s){

    ulong n = s.length-1;
    char c = s[n];

    if(['a', 'o', 'u'].canFind(c)){return s ~ 's';}
    if(c == 'i'){return s ~ ['o', 's'];}
    if(c == 'y'){
        s[n] = 'i';
        return s ~ ['o', 's'];
    }
    if(['l', 'r', 'v'].canFind(c)){return s ~ ['e', 's'];}
    if(c == 'n'){
        s[n] = 'a';
        return s ~ ['n', 'e', 's'];
    }
    if(c == 'e' && s[n-1] == 'n'){
        s[n-1] = 'a';
        s[n] = 'n';
        return s ~ ['e', 's'];
    }
    if(['t', 'w'].canFind(c)){return s ~ ['a', 's'];}
    return s ~ ['u', 's'];
}

void main(){
    
    int t;
    scanf("%d", &t);

    while(t--){
        word.latin.writeln;
    }
}
