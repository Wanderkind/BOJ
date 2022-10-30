import std.stdio;
import std.math;

void main(){
    
    int n,sum=0,k;
	readf!"%d\n"(n);
    
    foreach(i;0..n){
        readf!"%d\n"(k);
        sum+=pow(k/10,k%10);
	}

    writeln(sum);
}
