# include <stdio.h>

int main(void){
	
	int n,t,i,j,K,m,w;
	scanf("%d %d",&n,&K);
	int a[n];
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	for (i=0;i<K-1;i++){
		t=1;m=-1;
		for (j=0;j<n;j++){
			w=a[j];
			m=w>m?w:m;
		}
		for (j=0;j<n;j++){
			if (t){
				w=a[j];
				if (w==m){
					a[j]=-1;t=0;
				}
			}
		}
	}
	m=-1;
	for (i=0;i<n;i++){
		w=a[i];
		m=w>m?w:m;
	}
	printf("%d",m);
	return 0;
}
