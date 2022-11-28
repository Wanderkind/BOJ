import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


const char[21] cc = "ChongChong\0__________";
const char[21] bl = "_____________________";

void sol(){

    int n;
    char[21] a = bl, b = bl;
    bool A, B, C, noj;
    bool[char[21]] DANCE;

    scanf("%d", &n);
    while(n--){
        
        scanf("%s %s", &a, &b);
        A = (a in DANCE) != null;
        B = (b in DANCE) != null;
        noj = a != cc && b != cc;

        if(!(A || B)){
            
            if(noj){
                DANCE[a] = false;
                DANCE[b] = false;
            }
            else{
                DANCE[a] = true;
                DANCE[b] = true;
            }
        }

        else if(!A){
            
            if(noj){
                DANCE[a] = DANCE[b];
            }
            else{
                DANCE[a] = true;
                DANCE[b] = true;
            }
        }

        else if(!B){

            if(noj){
                DANCE[b] = DANCE[a];
            }
            else{
                DANCE[a] = true;
                DANCE[b] = true;
            }
        }

        else{
            
            C = DANCE[a] || DANCE[b];
            DANCE[a] = C;
            DANCE[b] = C;
        }

        a = bl; b = bl;
    }

    int ans = 0;
    foreach(i; DANCE){
        ans += i ? 1 : 0;
    }

    writeln(ans);
}

void main(){
    
    sol();
}
