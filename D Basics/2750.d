import std.algorithm;
import std.conv;
//import std.numeric;
import std.range;
import std.stdio;

void main(){
    
    int n,k;
    int[1000] a;
    scanf("%d\n",&n);
    
    foreach(i;0..n){
        scanf("%d",&k);
        a[i]=k;
    }

    int[] b=a[0..n];
    b.sort();
    
    foreach(i;b){
        writeln(i);
    }
}
