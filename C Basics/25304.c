# include <stdio.h>

int main(void){
	long long n,k,i,a,b,s=0;
	scanf("%lld",&n);
	scanf("%lld",&k);
	for(i=0;i<k;i++){
		scanf("%lld %lld",&a,&b);
		s+=a*b;
	}
	if (s==n){
		printf("Yes");
	}
	else{
		printf("No");
	}
	return 0;
}
