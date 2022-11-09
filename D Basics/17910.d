import std.stdio, std.algorithm.mutation, std.numeric;

void main(){
    long n,g,p=1L,q=0L;
    long[40] arr;
    readf!"%d"(n);
    
    foreach(i;0..n){
        scanf("%d",&arr[i]);
    }

    foreach_reverse(i;0..n){
        swap(p,q);
        p+=q*arr[i];
        g=gcd(p,q);
        p/=g;
        q/=g;
    }
    printf("%lld/%lld",p,q);
}
