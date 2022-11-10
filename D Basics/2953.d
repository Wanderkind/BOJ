import std.algorithm;
import std.conv;
//import std.numeric;
import std.range;
import std.stdio;


void main(){
    
    int[5] p;
    int[5] q;

    foreach(i;0..5){
        auto a = readln.splitter.map !(to !(int)).array;
        p[i]=sum(a);
        q[i]=sum(a);
    }
    sort(p[]);
    int k=p[4];
    
    foreach(i;0..5){
        if(k==q[i]){
            printf("%d %d",i+1,k);
        }
    }
}
