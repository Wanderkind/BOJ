import std.stdio;

void main(){
    int m,n,i,j=0;
    int[16] s=[48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70];
    int[20] arr;
    readf!"%d %d"(m,n);
    while(m){
        i=m%n;
        arr[j]=s[i];
        m/=n;
        j++;
    }
    if(j==0){
        writeln(0);
    }
    while(j--){
        printf("%c",arr[j]);
    }
}
