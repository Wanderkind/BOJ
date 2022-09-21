# include <stdio.h>
# define ll long long

const ll c0[4][4]= {{2,1,2,1},{3,2,3,2},{3,2,2,1},{4,3,3,2}};
const ll c1[4][4]= {{3,2,4,3},{4,3,5,4},{3,2,3,2},{4,3,4,3}};
const ll c2[4][4]= {{5,4,6,5},{6,5,7,6},{4,3,5,4},{5,4,6,5}};
const ll c3[4][4]= {{5,4,4,3},{6,5,5,4},{6,5,5,4},{7,6,6,5}};
const ll c4[4][4]= {{0,1,1,2},{1,0,2,1},{1,2,0,1},{2,1,1,0}};

ll l(ll i,ll j){
	if (i<2){
		return i+j-1;
	}
	else{
		return i-j-2;
	}
}

ll mod(ll a,ll b){
	if (a>=0){
		return a%b;
	}
	else{
		return (b-(-a%b))%b;
	}
}

ll f(ll X,ll Y,ll x,ll y){
	
	ll p,q;
	ll s,t,u,v,S,U;
	ll m,n,a,b,c,d,M,N,z;
	
	p=mod(X-2*mod(Y,5),5)-1;
	s=X+l(p,0);
	t=Y+l(p,1);
	
	q=mod(x-2*mod(y,5),5)-1;
	u=x+l(q,0);
	v=y+l(q,1);
	
	if (s>u){
		if (t>v){
			s=-s;
			t=-t;
			u=-u;
			v=-v;
			p=3-p;
			q=3-q;
		}
		else{
			S=t;U=v;
			t=-s;
			s=S;
			v=-u;
			u=U;
			p=(3-p)/2+2*(p%2);
			q=(3-q)/2+2*(q%2);
		}
	}
	else{
		if (t>v){
			S=-t;U=-v;
			t=s;
			s=S;
			v=u;
			u=U;
			p=p/2-2*(p%2-1);
			q=q/2-2*(q%2-1);
		}
	}
	
	m=u-s;
	n=v-t;
	if (m!=0||n!=0){
		if (n>3*m){
			b=m;
			c=(n-3*m)/5;
			z=3*b+5*c;
			M=c1[p][q]-3;
			N=c2[p][q]-5;
			if (b>0 && c>0){
				z+=M<N?M:N;
			}
			else{
				z+=M*(b>0?1:0)+N*(c>0?1:0);
			}
		}
		else if (2*n<m){
			a=n;
			d=(m-2*n)/5;
			z=2*a+5*d;
			M=c0[p][q]-2;
			N=c3[p][q]-5;
			if (a>0 && d>0){
				z+=M<N?M:N;
			}
			else{
				z+=M*(a>0?1:0)+N*(d>0?1:0);
			}
		}
		else{
			a=(3*m-n)/5;
			b=(n-a)/3;
			z=2*a+3*b;
			M=c0[p][q]-2;
			N=c1[p][q]-3;
			if (a>0 && b>0){
				z+=M<N?M:N;
			}
			else{
				z+=M*(a>0?1:0)+N*(b>0?1:0);
			}
		}
	}
	else{
		z=c4[p][q];
	}
	return z;
	
}

int main(void){
	
	ll i,C;
	ll X,Y,x,y,ans;
	scanf("%lld",&C);
	
	for(i=0;i<C;i++){
		scanf("%lld %lld %lld %lld",&X,&Y,&x,&y);
		ans=f(X,Y,x,y);
		printf("%lld\n",ans);
	}
	
	return 0;
	
}
