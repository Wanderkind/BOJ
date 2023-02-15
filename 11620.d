import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


float A (float xp, float yp, float xq, float yq) {
    
    if (xq <= 0.5 && 0.5 < xp) {
        float s = xp - xq;
        float t = xp - 0.5;
        float ans = (t*yq + (s-t)*yp)/s;
        return ans > 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float B (float xp, float yp, float xq, float yq) {
    
    if (xq <= -0.5 && -0.5 < xp) {
        float s = xp - xq;
        float t = xp + 0.5;
        float ans = (t*yq + (s-t)*yp)/s;
        return ans > 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float C (float xp, float yp, float xq, float yq) {
    
    if (yq <= 0.5 && 0.5 < yp) {
        float s = yp - yq;
        float t = yp - 0.5;
        float ans = (t*xq + (s-t)*xp)/s;
        return ans < 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float D (float xp, float yp, float xq, float yq) {
    
    if (yq <= -0.5 && -0.5 < yp) {
        float s = yp - yq;
        float t = yp + 0.5;
        float ans = (t*xq + (s-t)*xp)/s;
        return ans < 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float E (float xp, float yp, float xq, float yq) {
    
    if (xp < -0.5 && -0.5 <= xq) {
        float s = xq - xp;
        float t = -0.5 - xp;
        float ans = (t*yq + (s-t)*yp)/s;
        return ans < 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float F (float xp, float yp, float xq, float yq) {
    
    if (xp < 0.5 && 0.5 <= xq) {
        float s = xq - xp;
        float t = 0.5 - xp;
        float ans = (t*yq + (s-t)*yp)/s;
        return ans < 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float G (float xp, float yp, float xq, float yq) {
    
    if (yp < -0.5 && -0.5 <= yq) {
        float s = yq - yp;
        float t = -0.5 - yp;
        float ans = (t*xq + (s-t)*xp)/s;
        return ans > 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

float H (float xp, float yp, float xq, float yq) {
    
    if (yp < 0.5 && 0.5 <= yq) {
        float s = yq - yp;
        float t = 0.5 - yp;
        float ans = (t*xq + (s-t)*xp)/s;
        return ans > 0 ? ans : float.nan;
    }
    else {
        return float.nan;
    }
}

void main () {

    float[8] coord;
    foreach (i; 0..4) {
        scanf("%f %f", &coord[2*i], &coord[2*i + 1]);
    }
    
    float val;
    int Aseg, Bseg, Cseg, Dseg, Eseg, Fseg, Gseg, Hseg;
    float Apnt, Bpnt, Cpnt, Dpnt, Epnt, Fpnt, Gpnt, Hpnt;

    foreach (i; 0..4) {
        val = A(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Aseg = i;
            Apnt = val;
        }
    }

    foreach (i; 0..4) {
        val = B(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Bseg = i;
            Bpnt = val;
        }
    }

    foreach (i; 0..4) {
        val = C(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Cseg = i;
            Cpnt = val;
        }
    }

    foreach (i; 0..4) {
        val = D(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Dseg = i;
            Dpnt = val;
        }
    }

    foreach (i; 0..4) {
        val = E(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Eseg = i;
            Epnt = val;
        }
    }

    foreach (i; 0..4) {
        val = F(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Fseg = i;
            Fpnt = val;
        }
    }

    foreach (i; 0..4) {
        val = G(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Gseg = i;
            Gpnt = val;
        }
    }

    foreach (i; 0..4) {
        val = H(coord[2*i], coord[2*i + 1], coord[(2*i + 2) % 8], coord[(2*i + 3) % 8]);
        if (!isNaN(val)) {
            Hseg = i;
            Hpnt = val;
        }
    }

    float six, four, one, three;
    float x, y, X, Y;
    int key, KEY;

    if (abs(Cseg - Hseg + 1) == 2) {
        key = 2*Cseg;
        x = Hpnt - Cpnt;
        y = coord[key + 1] - 0.5;
        six = x*y/2;
    }
    else if (abs(Cseg - Hseg - 1) == 2) {
        KEY = 2*Cseg;
        key = (KEY + 2) % 8;
        x = Hpnt - Cpnt;
        y = 0.5 - coord[key + 1];
        six = 25 - x*y/2;
    }
    else {
        KEY = 2*Cseg;
        key = (KEY + 6) % 8;
        x = coord[key];
        y = coord[key + 1];
        X = coord[KEY];
        Y = coord[KEY + 1];
        six = 5*(hypot(x - Hpnt, y - 0.5) + hypot(X - Cpnt, Y - 0.5))/2;
    }

    if (abs(Eseg - Bseg + 1) == 2) {
        key = 2*Eseg;
        y = Bpnt - Epnt;
        x = -0.5 - coord[key];
        four = x*y/2;
    }
    else if (abs(Eseg - Bseg - 1) == 2) {
        KEY = 2*Eseg;
        key = (KEY + 2) % 8;
        y = Bpnt - Epnt;
        x = coord[key] + 0.5;
        four = 25 - x*y/2;
    }
    else {
        KEY = 2*Eseg;
        key = (KEY + 6) % 8;
        x = coord[key];
        y = coord[key + 1];
        X = coord[KEY];
        Y = coord[KEY + 1];
        four = 5*(hypot(y - Bpnt, x + 0.5) + hypot(Y - Epnt, X + 0.5))/2;
    }

    if (abs(Gseg - Dseg + 1) == 2) {
        key = 2*Gseg;
        x = Gpnt - Dpnt;
        y = -0.5 - coord[key + 1];
        one = x*y/2;
    }
    else if (abs(Gseg - Dseg - 1) == 2) {
        KEY = 2*Gseg;
        key = (KEY + 2) % 8;
        x = Gpnt - Dpnt;
        y = coord[key + 1] + 0.5;
        one = 25 - x*y/2;
    }
    else {
        KEY = 2*Gseg;
        key = (KEY + 6) % 8;
        x = coord[key];
        y = coord[key + 1];
        X = coord[KEY];
        Y = coord[KEY + 1];
        one = 5*(hypot(x - Dpnt, y + 0.5) + hypot(X - Gpnt, Y + 0.5))/2;
    }

    if (abs(Aseg - Fseg + 1) == 2) {
        key = 2*Aseg;
        y = Apnt - Fpnt;
        x = coord[key] - 0.5;
        three = x*y/2;
    }
    else if (abs(Aseg - Fseg - 1) == 2) {
        KEY = 2*Aseg;
        key = (KEY + 2) % 8;
        y = Apnt - Fpnt;
        x = 0.5 - coord[key];
        three = 25 - x*y/2;
    }
    else {
        KEY = 2*Aseg;
        key = (KEY + 6) % 8;
        x = coord[key];
        y = coord[key + 1];
        X = coord[KEY];
        Y = coord[KEY + 1];
        three = 5*(hypot(y - Fpnt, x - 0.5) + hypot(Y - Apnt, X - 0.5))/2;
    }

    float ans = (500 + 5*(6*six + 4*four + 1*one + 3*three))/124;
    printf("%.9f\n", ans);
}
