import std.stdio;
import core.stdc.stdlib;

long w, h, v, t, x, y, p, q;
long r, rsq, rw, rh;
long bot, top, tt, gg;
long zerotop, zerobot;

long f (long a, long b) {
    
    long c = a%2 ? (a + 1)*w - p - x : a*w + p - x;
    long d = b%2 ? (b + 1)*h - q - y : b*h + q - y;
    return c*c + d*d;
}

long rowscan (long z) {

    long left, right, pp, qq;

    left = 0; right = rw;
    while (true) {

        qq = (left + right)/2;
        gg = f(qq, z);

        if (rsq >= f(qq + 1, z) && rsq < f(qq + 2, z)) {
            qq++;
            break;
        }
        if (rsq >= gg && rsq < f(qq + 1, z)) {
            break;
        }
        if (rsq >= f(qq - 1, z) && rsq < gg) {
            qq--;
            break;
        }

        if (rsq >= gg) {
            left = qq;
        }
        else {
            right = qq;
        }
    }

    left = -rw; right = 0;
    while (true) {

        pp = (left + right)/2;
        gg = f(pp, z);

        if (f(pp - 2, z) > rsq && f(pp - 1, z) <= rsq) {
            pp--;
            break;
        }
        if (f(pp - 1, z) > rsq && gg <= rsq) {
            break;
        }
        if (gg > rsq && f(pp + 1, z) <= rsq) {
            pp++;
            break;
        }

        if (gg > rsq) {
            left = pp;
        }
        else {
            right = pp;
        }
    }
    
    return qq - pp + 1;
}

void main () {
    
    scanf(
        "%lld %lld %lld %lld %lld %lld %lld %lld",
        &w, &h, &v ,&t, &x, &y, &p, &q
    );

    r = v*t;
    rsq = r*r;
    rw = 2*r/w, rh = 2*r/h;

    if (f(0, 0) > rsq) {
        writeln(0);
        exit(0);
    }

    bot = 0; top = rh;
    while (true) {
        
        tt = (bot + top)/2;
        gg = f(0, tt);

        if (f(0, tt + 1) <= rsq && f(0, tt + 2) > rsq) {
            tt++;
            break;
        }
        if (gg <= rsq && f(0, tt + 1) > rsq) {
            break;
        }
        if (f(0, tt - 1) <= rsq && gg > rsq) {
            tt--;
            break;
        }

        if (rsq >= gg) {
            bot = tt;
        }
        else {
            top = tt;
        }
    }

    zerotop = tt;

    bot = -rh; top = 0;
    while (true) {
        
        tt = (bot + top)/2;
        gg = f(0, tt);

        if (f(0, tt - 1) <= rsq && f(0, tt - 2) > rsq) {
            tt--;
            break;
        }
        if (gg <= rsq && f(0, tt - 1) > rsq) {
            break;
        }
        if (f(0, tt + 1) <= rsq && gg > rsq) {
            tt++;
            break;
        }

        if (rsq >= gg) {
            bot = tt;
        }
        else {
            top = tt;
        }
    }

    zerobot = tt;

    long ans = 0, lr = 0, rl = 0, pp, qq;
    foreach_reverse (u; 0..zerotop + 1) {
        ans += rowscan(u);
    }

    foreach (u; zerobot..0) {
        ans += rowscan(u);
    }

    writeln(ans);
}
