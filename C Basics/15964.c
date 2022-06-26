#include <stdio.h>

int main(void)
{
	unsigned long long a;
	unsigned long long b;
	scanf("%ld", &a);
	scanf("%ld", &b);
	unsigned long long c = a*a-b*b;
	printf("%ld", c); 
	return 0;
}
