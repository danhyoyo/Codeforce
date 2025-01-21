#include <bits/stdc++.h>
using namespace std;
signed main(){
    int t; cin>>t;
    while(t--){
        int n, a[101]={0},max=0; cin>>n;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            a[x]++;
            if(a[x]>max){
                max=a[x];
            }
        }
        cout<<n-max<<endl;

    }
    return 0;
}