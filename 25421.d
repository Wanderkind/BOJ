import std.stdio;
import std.algorithm;


long m = 987654321;
long[9] blank = 0;
long[9][100000] dp;

long f(long n, long k) {
    
    long t = dp[n - 1][k - 1];
    if(t) return t;

    long ans = 0;
    foreach(i; max(1, k - 2)..min(10, k + 3)) {
        ans += f(n - 1, i);
    }
    ans %= m;
    dp[n - 1][k - 1] = ans;

    return ans;
}

void main() {

    dp = blank;
    dp[0] = 1;

    long n, ans = 0;
    scanf("%lld", &n);

    foreach(i; 1..10) {
        ans += f(n, i);
    }

    writeln(ans % m);
}
