#include <stdio.h>

int main(void)
{
	int a,b;
	scanf("%d\n%d",&a,&b);
	printf("%d\n",a*(b%10));
	printf("%d\n",a*(b/10%10));
	printf("%d\n",a*(b/100%10));
	printf("%d",a*b);
    return 0;
}
