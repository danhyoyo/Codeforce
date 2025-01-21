#include <bits/stdc++.h>
using namespace std;
int a[10001];
int main(){
    int n; cin>>n;
    int p, q;
    set<int> s;
    cin>>p;
    for(int i=0;i<p;i++){
        int x; cin>>x;
        s.insert(x);
    }
    cin>>q;
    for(int i=0;i<q;i++){
        int x; cin>>x;
        s.insert(x);
    }
    if(s.size()==n) cout<<"I become the guy.";
    else cout<<"Oh, my keyboard!";
    return 0;
}