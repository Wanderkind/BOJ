import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


int mod(int a, int b){
    return (a >= 0 ? a%b : (b-(-a%b))%b);
}

char[] word(){

    char[9] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..101){
        if (s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

void printboard(char[8][8] board, int x, int y, int dir){
    
    board[y][x] = ">^<v"[dir];

    foreach(i; 0..8){
        rank = board[i];
        foreach(j; 0..8){
            printf("%c", rank[j]);
        }
        writeln();
    }

    writeln();
}

char[8][8] board;
char[8] rank;

bool sol(){
    
    char c;
    char[] w;
    int y, x, dir;
    foreach(i; 0..8){
        w = word();
        if(w == "--"){return false;}
        rank = w;
        board[i] = rank;
        foreach(j; 0..8){
            
            c = rank[j];
            if(
                c == '>' ||
                c == '^' ||
                c == '<' ||
                c == 'v' ){
                y = i; x = j;

                if(c == '>'){dir = 0;}
                if(c == '^'){dir = 1;}
                if(c == '<'){dir = 2;}
                if(c == 'v'){dir = 3;}
            }
        }
    }

    int move, p;
    while(true){
        w = word();
        if(w == "move"){
            board[y][x] = '.';
            scanf("%d", &move);
            foreach(i; 0..move){
                p = 1;

                if(dir == 0 && x < 7){
                    if(board[y][x+1] != '.'){
                        while(x+p < 8 && board[y][x+p] != '.'){p++;}
                        foreach_reverse(j; x..x+p){
                            if(j < 7){
                                board[y][j+1] = board[y][j];
                            }
                        }
                    }
                    x++;
                }

                if(dir == 2 && 0 < x){
                    if(board[y][x-1] != '.'){
                        while(0 < x-p && board[y][x-p] != '.'){p++;}
                        foreach(j; x-p+1..x+1){
                            if(0 < j){
                                board[y][j-1] = board[y][j];
                            }
                        }
                    }
                    x--;
                }

                if(dir == 3 && y < 7){
                    if(board[y+1][x] != '.'){
                        while(y+p < 8 && board[y+p][x] != '.'){p++;}
                        foreach_reverse(j; y..y+p){
                            if(j < 7){
                                board[j+1][x] = board[j][x];
                            }
                        }
                    }
                    y++;
                }

                if(dir == 1 && 0 < y){
                    if(board[y-1][x] != '.'){
                        while(0 < y-p && board[y-p][x] != '.'){p++;}
                        foreach(j; y-p+1..y+1){
                            if(0 < j){
                                board[j-1][x] = board[j][x];
                            }
                        }
                    }
                    y--;
                }
            }
        }

        else if(w == "turn"){
            w = word();
            dir = mod((dir+(w == "left" ? 1 : (w == "back" ? 2 : -1))), 4);
        }

        else{
            break;
        }
    }

    printboard(board, x, y, dir);
    return true;
}

void main(){

    bool cont = true;
    while(cont){
        cont = sol();
    }
}
