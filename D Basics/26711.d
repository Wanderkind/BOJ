import std;

void main() {
    string a, b;
    readf!"%s\n%s\n"(a, b);
    writeln(BigInt(a) + BigInt(b));
}
