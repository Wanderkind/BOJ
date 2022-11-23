import std.stdio;
//import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

void main(){
    
    int n, k, R, C, r, c;
    int[2][100000] queens;
    scanf("%d %d", &n, &k);
    scanf("%d %d", &R, &C);

    foreach(i; 0..k){
        
        scanf("%d %d", &r, &c);
        queens[i] = [r, c];
    }

    bool check = false;
    
    foreach(i; 0..k){
        
        r = queens[i][0];
        c = queens[i][1];
        
        if(R == r || C == c || abs(R-r) == abs(C-c)){
            check = true;
        }
    }

    bool surrounded = true;
    bool scheck;
    int[2][8] periph = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]];
    int x, y;
    
    foreach(p; periph){
        
        x = R+p[0];
        y = C+p[1];

        if(1 <= x && x <= n && 1 <= y && y <= n){
            
            scheck = false;

            foreach(i; 0..k){
                
                r = queens[i][0];
                c = queens[i][1];
                
                if(x == r || y == c || abs(x-r) == abs(y-c)){
                    scheck = true;
                }
            }
            
            if(!scheck){
                surrounded = false;
            }
        }
    }

    if(check){
        writeln(surrounded ? "CHECKMATE" : "CHECK");
    }
    else{
        writeln(surrounded ? "STALEMATE" : "NONE");
    }
}
