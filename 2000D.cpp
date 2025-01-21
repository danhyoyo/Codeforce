#include <bits/stdc++.h>
using namespace std;
int a[200001];
signed main(){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        for(int i=1;i<=n;i++){
            int x; cin>>x;
            a[i]+=a[i-1]+x;
        }
        string s; cin>>s;
        cin.ignore();
        long long dem=0;
        for(int i=0,j=n-1; i<=j; i++, j--){
            while(s[i]=='R') i++;
            while(s[j]=='L') j--;
            if(i<j){
                dem+=a[j+1]-a[i];
            }
        }
        cout<<dem<<endl;
    }
    return 0;
}