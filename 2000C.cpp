#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n,m; cin>>n;
        vector<int> a;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            a.push_back(x);
        }
        cin>>m;
        while(m--){
            string s; cin>>s;
            bool b=true;
            if(s.length()==n){
                map<char, set<int>> mapchar;
                map<int, set<char>> mapint;
                for(int i=0;i<n;i++){
                    mapchar[s[i]].insert(a[i]);
                    mapint[a[i]].insert(s[i]);
                }
                for(auto x : mapchar){
                    set<int> setint = x.second;
                    if(setint.size()!=1) b=false;
                }
                for(auto x : mapint){
                    set<char> setchar = x.second;
                    if(setchar.size()!=1) b=false;
                }
                if(b) cout<<"YES"<<endl;
                else cout<<"NO"<<endl;
            } else cout<<"NO"<<endl;
        }
    }
    return 0;
}