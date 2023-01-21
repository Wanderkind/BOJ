import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;

long min(long a, long b){return a < b ? a : b;}

long howmany(long n, long k){
    
    long ans = 0;
    while(n%k == 0){
        ans++;
        n /= k;
    }

    return ans;
}

long d(long n, long a, long b){
    
    long ans = 0;
    while(n){
        ans += n/a;
        n /= a;
    }

    return ans/b;
}

void f(){

    long x, n, k = 2, h, ans = -1;
    scanf("%lld %lld", &x, &n);

    while(n > 1){
        
        if(k*k > n){
            if(ans == -1){
                ans = d(x, n, 1);
            }
            else{
                ans = min(ans, d(x, n, 1));
            }
            break;
        }
        else if(n%k == 0){
            h = howmany(n, k);
            if(ans == -1){
                ans = d(x, k, h);
            }
            else{
                ans = min(ans, d(x, k, h));
            }
            n /= pow(k, h);
        }
        else{
            k = k == 2 ? 3 : k+2;
        }
    }

    writeln(ans);
}

void main(){
    int t;
    scanf("%d", &t);
    while(t--){
        f();
    }
}
