#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n,x; cin>>n>>x;
        bool b=true;
        set<int> se;
        se.insert(x);
        n--;
        while(n--){
            int a; cin>>a;
            se.insert(a);
            if(! ((se.find(a-1)!=se.end()) || (se.find(a+1)!=se.end())) ) b=false;
        }
        if(b) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}