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

    long a, b, c, x, y, z;
    long A, B, C, X, Y, Z = -1;
    scanf("%ld %ld %ld", &c, &b, &a);
    scanf("%ld %ld %ld", &z, &y, &x);
    long s = a+b+c;

    while([a, b, c, x, y, z] != [A, B, C, X, Y, Z]){
        
        A = a; B = b; C = c; X = x; Y = y; Z = z;

        if(a>x){a = a-x; x = 0;} else{x = x-a; a = 0;}
        if(b>y){b = b-y; y = 0;} else{y = y-b; b = 0;}
        if(c>z){c = c-z; z = 0;} else{z = z-c; c = 0;}

        if(a){if(y<3*a){a -= y/3; y %= 3;} else{y -= 3*a; a = 0;}}
        if(b){if(z<3*b){b -= z/3; z %= 3;} else{z -= 3*b; b = 0;}}
        if(c){if(x<3*c){c -= x/3; x %= 3;} else{x -= 3*c; c = 0;}}

        if(a){if(z<9*a){a -= z/9; z %= 9;} else{z -= 9*a; a = 0;}}
        if(b){if(x<9*b){b -= x/9; x %= 9;} else{x -= 9*b; b = 0;}}
        if(c){if(y<9*c){c -= y/9; y %= 9;} else{y -= 9*c; c = 0;}}
    }
    
    writeln(s-a-b-c);
}

void main(){
    
    sol();
}
