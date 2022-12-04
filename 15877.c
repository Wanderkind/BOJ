# include <stdio.h>
# include <stdbool.h>

bool win(int a, int b){
	
    if(a+b == 0){
        return false;
    }

	if(a+b == 1){
        return true;
    }

    if(a>b){
        int c = a;
        a = b;
        b = c;
    }

    if(b<=2*a){
        int s = (a+b)%5;
        return s == 0 || s == 1 || s == 3;
    }

    if(a == 1 && b == 3){
        return true;
    }

    if(a%2){
        return true;
    }

    return b%2 == 1-(a%4)/2;
}

void sol(){
    
    int a, b;
    scanf("%d %d", &a, &b);

    printf(win(a, b)? "Alice" : "Bob");
}

int main(){

    sol();
    return 0;
}
