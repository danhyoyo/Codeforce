#include <bits/stdc++.h>
using namespace std;
int a[10001];
int main(){
    int t; cin>>t;
    while(t--){
        int a[4],n; cin>>a[0]>>a[1]>>a[2]>>n;
        sort(a,a+3);
        n=n-(a[2]-a[1])-(a[2]-a[0]);
        if(n>=0&&n%3==0) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}