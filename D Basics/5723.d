import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

bool leap(int y){

    if(y%400 == 0){
        return true;
    }
    if(y%100 == 0){
        return false;
    }
    if(y%4 == 0){
        return true;
    }
    return false;
}

const int[12] dim = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
];

int unit(int y, int m, int d){

    int ans = 0;
    
    foreach(i; 1900..y){
        ans += 365+leap(i);
    }

    foreach(i; 1..m){
        ans += dim[i-1];
        if(i==2 && leap(y)){ans++;}
    }

    return ans+d;
}

void sol(int n){

    int d, m, y, c;
    int D, M, Y, C;
    int u, U, diff, days, cons;
    bool know;
    n--;

    scanf("%d %d %d %d", &d, &m, &y, &c);
    u = unit(y, m, d);

    while(n--){
        
        scanf("%d %d %d %d", &D, &M, &Y, &C);
        U = unit(Y, M, D);
        diff = U-u;

        if(diff == 1){
            days++;
            cons += C-c;
            know = true;
        }
        else if(C == c){
            days += U-u+1-know;
            know = true;
        }
        else{
            know = false;
        }

        d = D; m = M; y = Y; c = C; u = U;
    }

    printf("%d %d\n", days, cons);
}

void main(){
    
    int n = 1;

    while(n){
        scanf("%d", &n);
        if(n){
            sol(n);
        }
    }
}
