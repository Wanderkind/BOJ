import std.stdio;

bool q(int N){
    int t=0,n=0,k=3;
    while(true){
        n=2*n+k;
        if(N<=n){
            return N>t+k?q(N-t-k):N==t+1;
        }
        k++;
        t=n;
    }
}

void main(){
    int N;
    readf!"%d"(N);
    writeln(q(N)?'m':'o');
}
