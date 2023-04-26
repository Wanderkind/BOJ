import std;


float x, y, c;

float f(float d) {
    return pow(x*x - d*d, -.5) + pow(y*y - d*d, -.5);
}

void main() {

    scanf("%f %f %f", &x, &y, &c);
    float l = 0, r = x < y ? x : y, t;

    foreach(_; 0..20) {
        t = (l + r)/2;
        if(f(t) > 1/c) r = t;
        else l = t;
    }

    printf("%.3f\n", t);
}
