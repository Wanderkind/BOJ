import std.stdio;

void f(int n,int s){
    foreach(_;0..n){
        printf ("%c", s);
    }
}

void s1(int n){
    foreach(_;0..n){
        f(n, 64);
        f(3*n, 32);
        f(n, 64);
        f(1, 10);
    }
}

void s2(int n){
    foreach(_;0..n){
        f(n, 64);
        f(2*n, 32);
        f(n, 64);
        f(1, 10);
    }
}

void s3(int n){
    foreach(_;0..n){
        f(3*n, 64);
        f(1, 10);
    }
}

void main(){
    int n;
    readf!"%d"(n);
    s1(n);s2(n);s3(n);s2(n);s1(n);
}
