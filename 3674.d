import std.stdio;
import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


double[2] trans(double x, double y, double ang){
    double c = cos(ang);
    double s = sin(ang);   
    return [x*c-y*s, x*s+y*c];
}

double Atan2(int y, int x){
    return atan2(cast(double)y, cast(double)x);
}

void sol(){
    
    int n, x, y, d;
    double f;
    int[2][] points;
    scanf("%d", &n);
    foreach(i; 0..n){
        scanf("%d %d", &x, &y);
        points ~= [x, y];
    }
    scanf("%d", &d);
    scanf("%lf", &f);

    double[] segs;
    foreach(i; 0..n-1){
        segs ~= hypot(cast(double)points[i+1][0]-points[i][0], cast(double)points[i+1][1]-points[i][1]);
    }
    double s = sum(segs);
    double Xorigin = cast(double)points[0][0], Yorigin = cast(double)points[0][1];
    double h = hypot(points[n-1][1]-Yorigin, points[n-1][0]-Xorigin);

    double[] segrat;
    foreach(i; 0..n-1){
        segrat ~= segs[i]/h;
    }

    double[] segrat2;
    foreach(i; 0..n-1){
        segrat2 ~= segs[i]/s;
    }
    
    double rattrack;
    int[] iterclct;
    foreach(_; 0..d){
        rattrack = 0;
        foreach(i; 0..n-1){
            rattrack += segrat2[i];
            if(f < rattrack){
                iterclct ~= i;
                f = 1 - ((rattrack-f)/segrat2[i]);
                break;
            }
        }
    }
    
    double[] rot;
    double cor = Atan2(points[n-1][1]-points[0][1], points[n-1][0]-points[0][0]);
    foreach(i; 0..n-1){
        rot ~= Atan2(points[i+1][1]-points[i][1], points[i+1][0]-points[i][0]) - cor;
    }
    
    double X = Xorigin, Y = Yorigin;
    double[2] nv;
    double R = 1, ang = 0;
    int w;
    foreach(i; iterclct){
        nv = trans(points[i][0]-Xorigin, points[i][1]-Yorigin, ang);
        X += R*nv[0]; Y += R*nv[1];
        R *= segrat[i];
        ang += rot[i];
        w = i;
    }
    
    nv = trans(points[w+1][0]-points[w][0],points[w+1][1]-points[w][1], ang-rot[w]);
    double k = f*R/segrat[w];
    X += k*nv[0]; Y += k*nv[1];
    
    printf("(%.9lf,%.9lf)\n", X, Y);
}

void main(){
    
    int t;
    scanf("%d", &t);
    while(t--){
        sol();
    }
}
