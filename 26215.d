import std.stdio;
import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;


int mx(int[] a, int n){
    
    int m = 0, ind, k;

    foreach(i; 0..n){

        k = a[i];
        if(k > m){
            m = k;
            ind = i;
        }
    }

    return ind;
}

int sx(int[] a, int n){
    
    int m = mx(a, n);
    a = a.dup.remove(m) ~ [];
    int s = mx(a, n);

    return s < m ? s : s+1;
}

int sol(){
	
    int n, k, s = 0, time = 0, v;
    int[100] a, b;
    scanf("%d", &n);

    foreach(i; 0..n){
        scanf("%d", &k);
        s += k;
        a[i] = k;
    }

    if(n == 1){
        return a[0] > 1440 ? -1 : a[0];
    }

    while(s && time < 1442){
        
        time++;
        v = sx(a, n);
        a[mx(a, n)]--;
        s--;

        if(a[v]){
            a[v]--;
            s--;
        }
    }

    return time > 1440 ? -1 : time;
}

void main(){

    writeln(sol());
}
