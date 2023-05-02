import std.stdio;

void main() {
	int w, h, x, y;
	scanf("%d %d %d %d", &w, &h, &x, &y);
	writeln(w%2 && h%2 && !((x + y)%2) ? "Lose" : "Win");
}
