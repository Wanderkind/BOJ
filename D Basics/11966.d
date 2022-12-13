import std;
void main(){
    int n;
    readf!"%d"(n);
    while(n%2-1){n>>=1;}
    writeln(n-1?0:1);
}
