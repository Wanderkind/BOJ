import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


bool[60] bin(long n){
    
    bool[60] i60;
    long k = 1152921504606846976;

    foreach_reverse(i; 0..61){
        
        if(n >= k){
            
            i60[i] = true;
            n -= k;
        }

        k >>= 1;
    }

    return i60;
}

long mod (long x) {
    return x % 1000000007;
}

long exp (long n, long k) {
    
    bool[60] B = bin(k);

    long ans = 1;
    long t = n;
    foreach (i; 0..60) {
        if (B[i]) {
            ans = (t*ans).mod;
        }
        t = (t*t).mod;
    }

    return ans;
}

long modInverse(long a, long b) {

    if (b == 1) {return 1;}
    
    long b0 = b, x0 = 0, x1 = 1, q, t;
    while (a > 1) {
        q = a / b;
        t = b;
        b = a % b;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    return (x1 < 0) ? (x1 + b0) : x1;
}

long vol (long n, long m) {

    long mul = (12*n - 16).mod;
    return exp(mul, m).mod;
}

long surf (long n, long m) {
    
    long p = 12*n - 16;
    long q =  4*n -  4;

    long ans = ((4*n-8).mod*exp(p, m)).mod;
    ans = (ans + exp(q, m+1)).mod;
    ans = (6*ans).mod;
    long x = modInverse(8*n-12, 1000000007);

    return (ans*x).mod;
}

void main () {
    
    long n, m;
    scanf("%ld %ld", &n, &m);
    printf("%ld %ld\n", vol(n, m), surf(n, m)); 
}
