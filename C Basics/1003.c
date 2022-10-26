# include <stdio.h>
# define ll long long

ll fib(ll n) {
    
	if (n<2){
		return n>0?n:-n;
	}
	else{
		ll a=0,b=1,c=0;
		int i;
		for(i=1;i<n;i++){
			c=a+b;
			a=b;
			b=c;
		}
		return c;
	}
}

int main(){
	
	int t,i;
	scanf("%d",&t);
	
	ll n;
	for(i=0;i<t;i++){
		
		scanf("%lld",&n);
		printf("%lld %lld\n",fib(n-1),fib(n));
	}
	
	return 0;
}
