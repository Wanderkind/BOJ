#include <stdio.h>

int f(int n){
	int a=n/10,b=n%10,c=a,i=0;
	a=b;
	b=(b+c)%10;
	c=a;
	return 10*a+b;
}

int main(void){
	int n,i=0;
	scanf("%d",&n);
	int N=n;
	do {
		n=f(n);
		i++;
	}while (f(N)!=f(n));
	printf("%d",i);
}
