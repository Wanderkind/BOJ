import std;
import core.stdc.stdlib;


long f(long n, long k, long p) {
    if(n == 1) return 0;
    if(n % k == 1) {
        long y = (n - 1)/k;
        if(y == 1) return 0;
        else if(y == k + 1) return p;
        else return f(y, k, p + 1);
    }
    return 0;
}

void main() {
    long n, d = 1, u, k, ans;
    double s1, s2;
    scanf("%ld", &n);
    s1 = sqrt(cast(double) n);
    while(d <= s1) {
        if(n % d == 0) {
            u = n/d;
            s2 = sqrt(cast(double) u);
            k = 2;
            while(k <= s2) {
                ans = f(u, k, 3);
                if(ans) {
                    writeln(ans);
                    foreach(i; 0..ans) printf("%ld ", d*k^^i);
                    exit(0);
                }
                k++;
            }
            s2 = sqrt(cast(double) d);
            k = 2;
            while(k <= s2) {
                ans = f(d, k, 3);
                if(ans) {
                    writeln(ans);
                    foreach(i; 0..ans) printf("%ld ", u*k^^i);
                    exit(0);
                }
                k++;
            }
        }
        d++;
    }
    writeln(-1);
}
