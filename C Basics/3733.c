#include <stdio.h>
#define ll unsigned long long

int main(void){
	ll a,b;
	while (scanf("%lld %lld",&a,&b)!=EOF){
		printf("%lld\n",b/(a+1));
	}
	return 0;
}
