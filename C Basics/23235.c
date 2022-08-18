#include <stdio.h>

int main(void)
{
	int i=0;
	char a[701];
	while(1){
		i++;
		fgets(a, 700, stdin);
		if(!strcmp(a,"0\n")){
			break;
		}
		printf("Case %d: Sorting... done!\n",i);
	}
	return 0;
}
