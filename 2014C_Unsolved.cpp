#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        long long tong=0;
        vector<int> v;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            v.push_back(x);
            tong+=x;
        }
        sort(v.begin(),v.end());
        if(n<=2) cout<<-1<<endl;
        else cout<<max((long long)0,(long long)-tong+1+n*v[n/2]*2)<<endl;
    }
    return 0;
}