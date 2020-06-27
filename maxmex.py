#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = 1e5 + 5; 
int t, n, m, a[N]; 

int main() {
  scanf("%d", &t); 
  while(t--) {
	scanf("%d %d", &n, &m); 
	
	set<int> st; 
	int ans = 0, x; 
	for(int i = 0; i < n; ++i) {
	  scanf("%d", &x); 
	  if(x != m) st.insert(x), ++ans; 
	}

	int mex = 1; 
	while(st.count(mex)) ++mex; 

	if(mex != m) ans = -1; 
	printf("%d\n", ans); 
  }
  return 0;
}