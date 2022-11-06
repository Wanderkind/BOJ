#include <stdio.h>;

void f(int n,int s){
    for(int i=0;i<n;i++){
        printf("%c", s);
    }
}

void s1(int n){
    for(int i=0;i<n;i++){
        f(n, 64);
        f(3*n, 32);
        f(n, 64);
        f(1, 10);
    }
}

void s2(int n){
    for(int i=0;i<n;i++){
        f(n, 64);
        f(2*n, 32);
        f(n, 64);
        f(1, 10);
    }
}

void s3(int n){
    for(int i=0;i<n;i++){
        f(3*n, 64);
        f(1, 10);
    }
}

int main(){
    int n;
    scanf("%d",&n);
    s1(n);s2(n);s3(n);s2(n);s1(n);
    return 0;
}
