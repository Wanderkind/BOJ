#include <stdio.h>

int f(int n){
	int N=n,s=n;
	while (n){
		s+=n%10;
		n/=10;
	}
	return s;
}

int main(void){
	int n,i,z;
	for (n=0;n<=10000;++n){
		z=1;
		for(i=0;i<10000;i++){
			if (f(i)==n){
				z=0;
				break;
			}
	 	}
		if (z){
			printf("%d\n",n);
		}
	}
	return 0;
}
