# include <stdio.h>
# define int long

int arr[1000001];

int f(int n){
	
    if(arr[n]){
        return arr[n]-1;
    }
	
    if(n==1){
        arr[n] = 1;
        return 0;
    }
	
    int F, m = f(n-1)+1;
	
    if(n%3==0){
        F = f(n/3)+1;
        if(F < m){
        	m = F;
		}
    }
    if(n%2==0){
        F = f(n/2)+1;
        if(F < m){
        	m = F;
		}
    }
	
    arr[n] = m+1;
    return m;
}

int main(){
	
    int n;
	scanf("%d", &n);
    printf("%d", f(n));
    
    return 0;
}
