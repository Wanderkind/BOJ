import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

int sol(double f){
    double s=0.0;
    double i=1.0;
    while(s<f){
        i+=1.0;
        s+=1/i;
    }
    return cast(int)(i-1.0);
}

void main(){
    
    int c;
    double f=1.0;
    while(f){
        scanf("%lf",&f);
        if(f){
            c=sol(f);
            printf("%d card(s)\n",c);
        }
    }
}
