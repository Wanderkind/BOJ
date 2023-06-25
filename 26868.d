import std;


void main() {

    int a, b, cnt = 1;
    scanf("%d %d", &a, &b);
    int g = gcd(a, b);
    a /= g;  b /= g;
    a = a*a; b = b*b;

    string[] st;
    if(a > b) {
        st ~= "atan sin acos tan ";
        swap(a, b);
        cnt += 4;
    }

    while(a*b > 1) {
        cnt += 2;
        if(2*a > b){
            st ~= "atan cos ";
            b = b - a;
            swap(a, b);
        }
        else {
            st ~= "atan sin ";
            b = b - a;
        }
        g = gcd(a, b);
        a /= g;  b /= g;
    }

    writeln(cnt);
    write("cos ");
    foreach_reverse(s; st) write(s);
}
