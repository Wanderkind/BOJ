# include <stdio.h>
#include <string.h>

int f(float a,float b){
	
	int r=16*((int)(a/22.5))+(int)(b/22.5);
	return r;

}

int main(){
	
	char str[25003]="";
	char r;
	int n,i;
	float a,b;
	
	scanf("%d",&n);
	for (i=0;i<n/2;i++){
		scanf("%f\n%f",&a,&b);
		r=f(a,b);
		strncat(str,&r,1);
	}
	
	printf("%s",str);
	
	return 0;
}
