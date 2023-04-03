import std.stdio;


void main () {
    
    long n;
    scanf("%lld", &n);
    long d = n/2;
    long r = d*d;
    long a = 0, x = 0, y = d - 1, yy;

    while (y) {
        
        yy = y*y;
        
        if (x*x + yy == r) {
            y--;
            a++;
        }
        else if ((x + 1)*(x + 1) + yy > r) {
            y--;
        }
        else {
            x++;
        }
    }
    
    writeln(4*(n - a - 1));
}
