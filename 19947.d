import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


int f(int h, int y){
    
    if(!y){
        return h;
    }

    int k, m = h;

    k = f(21*h/20, y-1);
    if(k > m){m = k;}
    
    if(y>2){
        k = f(6*h/5, y-3);
        if(k > m){m = k;}
    }
    
    if(y>4){
        k = f(27*h/20, y-5);
        if(k > m){m = k;}
    }
    
    return m;
}

void main(){
	
    int  h, y;
	scanf("%d %d", &h, &y);

    writeln(f(h, y));
}
