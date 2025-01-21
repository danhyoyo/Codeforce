#include <bits/stdc++.h>
using namespace std;
signed main(){
    int t; cin>>t;
    while(t--){
        int n,a[50]; cin>>n;
        for (int i=0;i<n;i++){
            cin>>a[i];
        }
        if(n>2) cout<<"NO"<<endl;
        else{
            if(a[1]-a[0]==1) cout<<"NO"<<endl;
            else cout<<"YES"<<endl;
        }
    }
    return 0;
}