import std.algorithm;
import std.conv;
//import std.numeric;
import std.range;
import std.stdio;

void main(){
    
    auto a = readln.splitter.map !(to !(int)).array;
    a.sort();
    
    foreach(i;a){
        printf("%d ",i);
    }
}
