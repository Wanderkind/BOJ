import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


bool[] bin (long n) {
    
    bool[] ans;
    long k = 1;
    int c = 1;
    while (k < n) {
        k <<= 1;
        c++;
    }

    while (c) {
        if (n >= k) { 
            ans ~= true;
            n -= k;
        }
        else{
            ans ~= false;
        }
        k >>= 1;
        c--;
    }

    return ans.reverse;
}

long[4] mul (long[4] a, long[4] b) {
    return [
        a[0]*b[0] + a[1]*b[2],
        a[0]*b[1] + a[1]*b[3],
        a[2]*b[0] + a[3]*b[2],
        a[2]*b[1] + a[3]*b[3]
    ];
}

long l (long n) {
    
    long[4] l = [1, 1, 1, 0];
    long[4] L = [1, 0, 0, 1];
    bool[] B = bin(n);
    foreach (i; 0..B.length) {
        if (i) {l = mul(l[0..4], l[0..4]);}
        if (B[i]) {L = mul(L[0..4], l[0..4]);}
    }

    return 4*L[1] - 2;
}

long l83 = l(83), l84 = l(84);

void sol (long n, long k) {
    
    long ln = l(n);

    if (n < 85) {
        if (k > ln) {
            writeln('0');
        }
        else {
            if (k == 1) {
                writeln('(');
            }
            else if (k == ln) {
                writeln(')');
            }
            else {
                long status = n - 2, loc = k - 1;
                loc <= l(status) ? sol(status, loc) : sol(status + 1, loc - l(status));
            }
        }
    }
    else {
        long d = (n - 83)/2, newk = k - d;
        if (newk < 1) {
            writeln('(');
        }
        else if (n % 2 == 1) {
            newk > l83 ? sol(84, newk - l83) : sol(83, newk);
        }
        else {
            newk > l84 ? sol(85, newk - l84) : sol(84, newk);
        }
    }
}

void main () {

    int t;
    scanf("%d", &t);

    long n, k;
    while (t--) {
        scanf("%lld %lld", &n, &k);
        sol(n, k);
    }
}
