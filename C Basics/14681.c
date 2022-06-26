#include <stdio.h>

int main(void)
{
	int a;
	int b;
	scanf("%d", &a);
	scanf("%d", &b);
	int A = a>0;
	int B = b>0;
	printf("%d", -2*A*B+A-B+3);
	return 0;
}
