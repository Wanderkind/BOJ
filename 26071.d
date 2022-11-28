import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


void sol(){

    int n, a, b, c, d;
    int A = 0, B = 0, C = 0, D = 0;
    int X = 1500, Y = 1500;
    scanf("%d", &n);
    char[1501] k;

    foreach(i; 0..n){
        
        scanf("%s", &k);
        foreach(j; 0..n){
            
            if(k[j] == 'G'){
                
                a = i;
                b = n-1-i;
                c = j;
                d = n-1-j;

                if(a>A){A=a;}
                if(b>B){B=b;}
                if(c>C){C=c;}
                if(d>D){D=d;}

                if(a<X){X=a;}
                if(c<Y){Y=c;}
            }
        }
    }
    
    if(A==X && C==Y){writeln(0);}
    else if(A==X){writeln(min(C, D));}
    else if(C==Y){writeln(min(A, B));}
    else{writeln(min(A+C, A+D, B+C, B+D));}
}

void main(){
    
    sol();
}
