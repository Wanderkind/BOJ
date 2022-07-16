#include <stdio.h>

int main(void){
	int n,i,j;
	scanf("%d",&n);
	if (n==1){
		printf("*");
	}
	else {
		for (i=0;i<n;i++){
			for (j=0;j<(n+1)/2;j++){
				printf("* ");
			}
			printf("\n");
			for (j=0;j<(n+1)/2-(n%2);j++){
				printf(" *");
			}
			printf("\n");
		}
	}
	return 0;
}
