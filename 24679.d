import std.stdio;
import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;
//import core.stdc.stdlib;


bool win(int x, int y, int z){
	
	int d = abs(y-z);

    if(x%2){
        
        if(y+z < x+2){
            
            if(max(y, z) == x && y+z == x+1){
                return false;
            }

            return (y%2 + z%2)>0;
        }

        if(d < max(x-1, 1)){

            if((y+z-x-1)%4){
                return true;
            }

            return false;
        }

        return true;
    }

    if(y+z < x+3){
        return (y%2 + z%2)>0;
    }

    if(x%4){

        if((y+z)%4 == 2){
            return !(d%4);
        }

        if((y+z)%4 == 0){
            return d%4>0;
        }

        if((y+z)%4 == 1){
            return d > x && d%4 == 3;
        }

        if(d < x){
            return true;
        }

        return d%4 == 1;
    }

    else{
        
        if((y+z)%4 == 2){
            return !(d%4);
        }

        if((y+z)%4 == 0){
            return d%4>0;
        }

        if((y+z)%4 == 3){
            return d > x && d%4 == 1;
        }

        if(d < x){
            return true;
        }

        return abs(y-z)%4 == 3;
    }
}

void sol(){
    
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);

    writeln(win(x, y, z)? "R" : "B");
}

void main(){
    
    int t;
    scanf("%d", &t);

    while(t--){
       sol();
    }
}
