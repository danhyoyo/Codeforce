#include <bits/stdc++.h>
using namespace std;
void solve(int n, int k){
    long long p=(n+n-k+1)*k/2;
    if(p%2==0) cout<<"YES";
    else cout<<"NO";
    cout<<endl;
}
int main(){
    int t; cin>>t;
    while(t--){
        int n,k; cin>>n>>k;
        solve(n,k);
    }
    return 0;
}