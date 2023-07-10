import std;


long mod = 10^^9 + 7;

long pow(long p, long q) {
    bool[] b;
    long sub = p % mod, ans = 1;
    while(q) {
        if(q % 2) ans = ans*sub % mod;
        sub = sub*sub % mod;
        q >>= 1;
    }
    return ans;
}

void main() {
    long n, a;
    scanf("%ld %ld", &n, &a);
    long p = pow(n, a + 1)*(n - 1) % mod;
    long q = pow(n - 1, a)*(n*(n - 2) % mod) % mod;
    writeln((mod + p - q) % mod);
}
