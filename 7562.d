import std.stdio;
import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

int nrm(int a,int b){
    
    if(a>b){
        swap(a,b);
    }

    if(a==0 && b<4){
        return [0,3,2,3][b];
    }
    if(a==b && b<4){
        return [0,2,4,2][b];
    }

    if(a*2<=b){
        if(a%2){
            return b-1-(2*((b-2)/4));
        }
        else{
            return b-(2*(b/4));
        }
    }
    else{
        int c=a+b;
        if(c%2){
            return 1+2*((c/2+1)/3);
        }
        else{
            return 2*((c/2+2)/3);
        }
    }
}

void sol(){
    
    int k,x,y,X,Y;
    scanf("%d",&k);
    scanf("%d %d",&x,&y);
    scanf("%d %d",&X,&Y);
    int a=abs(x-X),b=abs(y-Y);
    
    if([
        [0,0,1,1],
        [1,1,0,0],
        [0,k-1,1,k-2],
        [1,k-2,0,k-1],
        [k-1,0,k-2,1],
        [k-2,1,k-1,1],
        [k-1,k-1,k-2,k-2],
        [k-2,k-2,k-1,k-1]
    ].canFind([x,y,X,Y]) ){
        writeln(4);
    }
    else if(
        (!((x+X)*(x+X-2*k+2)) && b==3) ||
        (!((y+Y)*(y+Y-2*k+2)) && a==3) ){
        writeln(5);
    }
    else{
        writeln(nrm(a,b));
    }
}

void main(){
    
    int n;
    scanf("%d",&n);
    
    while(n--){
        sol();
    }
}
