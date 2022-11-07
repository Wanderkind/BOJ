import std.stdio;

int last(int n, int d){
    return n%10==d?1:0;
}

int count(int n, int d){
    return last(n,d)+(n<10?0:count(n/10,d));
}

int sol(int l, int r, int d){
    return count(l,d)+(l==r?0:sol(l+1,r,d));
}

void main(){
    int l,r,d;
    readf!"%d %d %d"(l,r,d);
    writeln(sol(l,r,d));
}
