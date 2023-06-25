import std;


bool sol() {

    double w, h;
    scanf("%lf %lf", &w, &h);
    if(!w && !h) return false;

    double pi = cast(double) PI;
    
    double x = w/pi;
    double v1 = (h - x)*x*x*pi/4;

    double y = min(h/(pi + 1), w);
    double v2 = w*y*y*pi/4;

    printf("%.3lf\n", max(v1, v2));
    return true;
}

void main() {

    bool cont = true;
    
    while(cont) cont = sol();
}
