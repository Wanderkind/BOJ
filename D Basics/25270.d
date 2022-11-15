import std.stdio;
//import std.algorithm;
//import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

int mod(int a,int b){
	if (a>=0){
		return a%b;
	}
	else{
		return (b-(-a%b))%b;
	}
}

void main(){
    
    int n,a,b;
    scanf("%d",&n);
    a = n;
    b = n;
    while(mod(a,100)<99){
        a++;
    }
    while(mod(b,100)<99){
        b--;
    }
    writeln(a-n<=n-b?a:(b>0?b:a));
}
