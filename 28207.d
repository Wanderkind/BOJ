import std;


int[3][6] cn = [
    [0, 1, 2], [1, 2, 0], [0, 2, 1],
    [1, 0, 2], [2, 1, 0], [2, 0, 1] 
];
int[3] r1 = [0,   0, 255];
int[3] r2 = [0, 255, 255];

void render(double x0, double y0, double z0, int k) { // assumes x <= y <= z

    double y1 = 255*min((y0 - x0)/(255 - x0), 1);
    double z1 = 255*min((z0 - x0)/(255 - x0), 1);
    double z2 = 255*min((z1 - y1)/(255 - y1), 1);
    if(isNaN(z2)) z2 = 255;

    //printf("y1 = %.9f, z1 = %.9f, z2 = %.9f\n", y1, z1, z2); ////////
    int[3] ind = cn[k];
    int a = ind[0], b = ind[1], c = ind[2];

    writeln(3);
    printf("%d %d %d %.9lf\n", r1[a], r1[b], r1[c], max(z2, 0));
    printf("%d %d %d %.9lf\n", r2[a], r2[b], r2[c], hypot(y1, z2 - z1));
    printf("255 255 255 %.9lf\n", hypot(x0, y0 - y1, z0 - z1));
}

void sol() {

    double r, g, b;
    scanf("%lf %lf %lf", &r, &g, &b);

    if(r == g && g == b) { // exception
        printf("1\n255 255 255 %.9lf\n", r*sqrt(3.));
    }
    else if(r <= g) {
        if(g <= b)      render(r, g, b, 0);
        else if(b <= r) render(b, r, g, 1);
        else            render(r, b, g, 2);
    }
    else {
        if(r <= b)      render(g, r, b, 3);
        else if(b <= g) render(b, g, r, 4);
        else            render(g, b, r, 5);
    }
}

void main() {

    int t;
    scanf("%d", &t);

    while(t--) {
        sol();
    }
}
