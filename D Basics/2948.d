import std.stdio;

int[12] k=[31,28,31,30,31,30,31,31,30,31,30,31];
string[7] D=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"];

void main(){
    int d,m;
    readf!"%d %d"(d,m);
    
    foreach(i; 0..m-1){
        d+=k[i];
    }

    writeln(D[(d+2)%7]);
}
