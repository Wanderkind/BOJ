# include <stdio.h>
# include <math.h>
# define ll long long

ll f(ll x,ll y) {
    
	ll k=y-x;
	ll n=ceil(pow(k+.25,.5)-.5);
	
	return 2*n-(k<=n*n);
}

int main(){
	
	int t;
	scanf("%d",&t);
	
	ll x,y;
	while(t--){
		
		scanf("%lld %lld",&x,&y);
		printf("%lld\n",f(x,y));
	}
	
	return 0;
}
