#include <stdio.h>

int main(void)
{
	unsigned long long a;
	unsigned long long b;
	scanf("%lld", &a);
	scanf("%lld", &b);
	unsigned long long c = a*a-b*b;
	printf("%lld", c); 
	return 0;
}
