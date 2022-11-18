# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>

int nrm(int a,int b){
    
    int p[4]={0,3,2,3};
    int q[4]={0,2,4,2};
    
    if(a>b){
        int u;
        u=a;
        a=b;
        b=u;
    }

    if(a==0 && b<4){
        return p[b];
    }
    if(a==b && b<4){
        return q[b];
    }

    if(a*2<=b){
        if(a%2){
            return b-1-(2*((b-2)/4));
        }
        else{
            return b-(2*(b/4));
        }
    }
    else{
        int c=a+b;
        if(c%2){
            return 1+2*((c/2+1)/3);
        }
        else{
            return 2*((c/2+2)/3);
        }
    }
}

bool eq(int* a, int* b){
	
	bool yes=
		a[0]==b[0] &&
		a[1]==b[1] &&
		a[2]==b[2] &&
		a[3]==b[3] ;
	
	return yes;
}

void sol(){
    
    int i=0,k,x,y,X,Y;
    scanf("%d",&k);
    scanf("%d %d",&x,&y);
    scanf("%d %d",&X,&Y);
    int a=abs(x-X),b=abs(y-Y);
    
    int v[4]={x,y,X,Y};
    int w[8][4]={
        {0,0,1,1},
        {1,1,0,0},
        {0,k-1,1,k-2},
        {1,k-2,0,k-1},
        {k-1,0,k-2,1},
        {k-2,1,k-1,1},
        {k-1,k-1,k-2,k-2},
        {k-2,k-2,k-1,k-1}
    };
    bool yes=false;
    
    while(!yes && i<8){
    	yes=eq(v,w[i]);
    	i++;
	}
	
    if(yes){
    	printf("%d",4);
	}
    else if(
        (!((x+X) && (x+X-2*k+2)) && b==3) ||
        (!((y+Y) && (y+Y-2*k+2)) && a==3) ){
        printf("%d",5);
    }
    else{
        printf("%d",nrm(a,b));
    }
    printf("\n");
}

int main(){
    
    int n;
    scanf("%d",&n);
    
    while(n--){
        sol();
    }
    
    return 0;
}
