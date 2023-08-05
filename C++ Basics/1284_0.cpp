# include <iostream>
using namespace std;

bool sol() {
	
	int n, k, ans = 1; cin >> n;
	if(!n) return false;
	
	while(n) {
		k = n % 10;
		ans += k > 1 ? 4 : (k ? 3 : 5);
		n /= 10;
	}
	
	cout << ans << endl;
	return true;
}

int main() {
	/*
	ios_base :: sync_with_stdio(false); 
	cin.tie(NULL); 
	cout.tie(NULL);
	*/
	bool cont = true;
	while(cont) cont = sol();
	
	return 0;
}
