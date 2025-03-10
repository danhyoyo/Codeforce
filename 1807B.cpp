#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n, a[101],c = 0, l = 0; cin>>n;
        for(int i = 0;i < n; i++){
            cin>>a[i];
            if (a[i]&1==1){
                l+=a[i];
            }
            else c+=a[i];
        }
        if (c>l){
            cout<<"YES"<<endl;
        } else cout<<"NO"<<endl;

    }
    return 0;
}