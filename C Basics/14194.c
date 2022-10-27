# include <stdio.h>
# include <stdlib.h>

int min(int n,int arr[n]){
	
	int m=100;
	int i;
	
	for(i=0;i<n;i++){
		int k=arr[i];
		if(k<m){
			m=k;
		}
	}
	
	return m;
}

int max(int n,int arr[n]){
	
	int m=0;
	int i;
	
	for(i=0;i<n;i++){
		int k=arr[i];
		if(k>m){
			m=k;
		}
	}
	
	return m;
}

int sum(int n,int arr[n]){
	
	int s=0;
	int i;
	
	for(i=0;i<n;i++){
		s+=arr[i];
	}
	
	return s;
}

void sol(){
	
	int n,i;
	scanf("%d",&n);
	
	int arr[n];
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	
	int m=min(n,arr);
	int M=max(n,arr);
	int A=2*sum(n,arr);
 	int B=n*(m+M);
	
	printf(abs(A-B)<2*n?"Yes\n":"No\n");
}

int main(){
	
	int n,i;
	scanf("%d",&n);
	
	for(i=0;i<n;i++){
		sol();
	}
	return 0;
}
