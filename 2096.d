import std;


void main() {

    int n;
    scanf("%d", &n);

    int a, b, c, d, e, f, g, h, i;
    int A, B, C, D, E, F, G, H, I;
    scanf("%d %d %d", &a, &b, &c);
    A = a; B = b; C = c;

    foreach(_; 1..n) {
        scanf("%d %d %d", &d, &e, &f);
        D = d; E = e; F = f;
        
        g = d + min(a, b);    G = D + max(A, B);
        h = e + min(a, b, c); H = E + max(A, B, C);
        i = f + min(b, c);    I = F + max(B, C);
        a = g; b = h; c = i;
        A = G; B = H; C = I;
    }
    printf("%d %d", max(A, B, C), min(a, b, c));
}
