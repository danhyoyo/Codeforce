#include <bits/stdc++.h>
using namespace std;
string solve(map<int,int> mp){
    for(auto it:mp){
        if((it).second%2==1) return "YES";
    }
    return "NO";
}
int main(){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        map<int,int> mp;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            if(mp.find(x)!=mp.end()) mp[x]++;
            else mp.insert({x,1});
        }
        cout<<solve(mp)<<endl;
    }
    return 0;
}