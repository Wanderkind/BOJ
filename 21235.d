import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


int mod(int a, int b){
    return (a >= 0 ? a%b : (b-(-a%b))%b);
}
int div(int a, int b){
    return (a >= 0 ? a/b : (a+(-a%b))/b-1);
}

char[] word(){

    char[11] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..11){
        if (s[i] == ' ' || s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

string[12] zodiac = [
    "Ox", "Tiger", "Rabbit", "Dragon",
    "Snake", "Horse", "Goat", "Monkey",
    "Rooster", "Dog", "Pig", "Rat"
];

void main(){
    
    int n, r, y;
    char[] n1, n2, zod;
    bool next;
    int[string] l = ["Bessie": 0];
    
    scanf("%d", &n);
    foreach(i; 0..n){
        
        n1 = word();
        word(); word();
        next = word() == "next";
        zod = word();
        word(); word();
        n2 = word();
        
        foreach(j; 0..12){
            if(zod == zodiac[j]){r = j; break;}
        }

        y = l[n2];
        if(next){
            l[cast(string)n1] = (div(y, 12)+(r <= mod(y, 12)))*12+r;
        }
        else{
            l[cast(string)n1] = (div(y, 12)-(r >= mod(y, 12)))*12+r;
        }
    }
    
    writeln(abs(l["Elsie"]));
}
