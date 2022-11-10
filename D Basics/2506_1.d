import std.algorithm;
import std.conv;
//import std.numeric;
import std.range;
import std.stdio;

void main(){
    
    int n,z=0,sum=0;
    scanf("%d\n",&n);
    auto a = readln.splitter.map !(to !(int)).array;
    
    foreach(k;a){
        z=(k?z+1:0);
        sum+=z*k;
    }
    
    writeln(sum);
}
