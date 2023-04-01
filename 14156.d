import std.stdio;


long n;

long f (long x) {

    long ans = 1;

    for (; x%2 == 0; x >>= 1) {
        ans <<= 1;
    }

    return ans;
}

void printbin (long x) {
    
    for (long i = 1 << (n - 1); i; i >>= 1) {
        printf("%d", x & i ? 1 : 0);
    }

    writeln();
}

void main () {

    scanf("%lld", &n);

    long k, x = 0, t = (1 << n) + 1;
    foreach (i; 1..t) {
        k = f(i);
        printbin(x);
        x ^= k;
    }
}
