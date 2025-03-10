#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n, a, b; cin>>n>>a>>b;
        cout<<min(a*n, b*int(n/2)+(n%2)*a)<<endl;
    }
    return 0;
}