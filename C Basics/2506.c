# include <stdio.h>

int main(){
    int n,k,z=0,sum=0;
    scanf("%d",&n);
    while(n--){
    	scanf("%d",&k);
    	z=(k?z+1:0);
    	sum+=z*k;
	}
	printf("%d",sum);
	return 0;
}
