import std.stdio;

void main(){
	int n;
	readf!("%d")(n);
	foreach(i;1..10){
		writeln(n," * ",i," = ",n*i);
	}
}
