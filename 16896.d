import std.stdio;

void main(){

	int t;
	scanf("%d", &t);
	
	long n;
	while(t--) {
		scanf("%lld", &n);
		writeln(n % 2 && !(1537228672809129300 & n) ? "koosaga" : "cubelover");
	}
}
