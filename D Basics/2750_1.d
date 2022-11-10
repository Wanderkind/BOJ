import std.algorithm;
import std.conv;
//import std.numeric;
import std.range;
import std.stdio;

void main(){

    int n;
    scanf("%d",&n);
    int[1000] a;

    foreach(i;0..n){
        scanf("%d",&a[i]);
    }

    int[] b=a[0..n];
    sort(b);

    foreach(i;b){
        writeln(i);
    }
}
