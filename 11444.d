import std.stdio;
//import std.algorithm;
//import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

long w = 1000000007;

long[2][2] mul(long[2][2] A, long[2][2] B){
    
    long s;
    long[2][2] L;
    foreach(i; 0..2){
        
        long[2] a = A[i];
        long[2] l;

        foreach(j; 0..2){
            
            long[2] b = [B[0][j], B[1][j]];
            s = 0L;

            foreach(k; 0..2){
                s += (a[k]%w)*(b[k]%w);
            }

            l[j] = s%w;
        }

        L[i] = l;
    }

    return L;
}

bool[60] bin(long n){
    
    bool[60] i60;
    long k = 1152921504606846976L;

    foreach_reverse(i; 0..61){
        
        if(n >= k){
            
            i60[i] = true;
            n -= k;
        }

        k >>= 1;
    }

    return i60;
}

long sol(long n){
    
    bool[60] B = bin(n);
    long[2][2] K = [[1L,0L],[0L,1L]];
    long[2][2] L = [[1L,1L],[1L,0L]];

    int l=59;
    while(!(B[l])){
        l--;
    }

    foreach(i; 0..l+1){
        
        if (i){
            L = mul(L, L);
        }
        if (B[i]){
            K = mul(K, L);
        }
    }

    return K[0][1];
}

void main(){
    
    long n;
    scanf("%ld", &n);

    writeln(sol(n));
}
