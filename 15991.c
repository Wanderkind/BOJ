#include <stdio.h>
#define M 1000000009

int main(void){
	int N,n,h,i;
	long long a,b,c,d;
	scanf("%d",&N);
	for (h=0;h<N;h++){
		scanf("%d",&n);
		a=0,b=1,c=0,d=1;
		for (i=0;i<n/2+1;i++){
			d=(a%M+b%M+c%M)%M;a=b;b=c;c=d;
			}
		printf("%d\n",d);
	}
	return 0;
}
