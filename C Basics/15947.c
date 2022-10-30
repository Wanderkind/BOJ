# include <stdio.h>
//# include <math.h>
//# define ll long long

char l[14][10]={
	"baby","sukhwan","tururu","turu",
	"very","cute","tururu","turu",
	"in","bed","tururu","turu",
	"baby","sukhwan"
};

int main(){
	
	int n;
	scanf("%d",&n);
	n--;
	
	int a=n/14;
	int b=n%14;
	int c=b%4;
	
	if (c>1){
		if (c-a>-1){
			printf(l[b]);
			while (a--){
				printf("ru");
			}
		}
		else{
			printf("tu+ru*%d",a-c+4);
		}
	}
	else{
		printf(l[b]);
	}
	
	return 0;
}
