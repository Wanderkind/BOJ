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

    sort(a[0..n]);

    foreach(i;a[0..n]){
        writeln(i);
    }
}
