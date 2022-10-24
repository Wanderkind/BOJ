import std.stdio;

void main(){
	int a,b,c;
	readf!("%d %d %d")(a,b,c);
	int d=(a+1)*(b+1)/(c+1)-1;
	writeln(d);
}
