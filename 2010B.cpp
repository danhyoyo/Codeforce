#include <bits/stdc++.h>
using namespace std;
int main(){
    set<int> s;
    int a,b; cin>>a>>b;
    s.insert(a); s.insert(b);
    if(s.find(1)==s.end()) cout<<1;
    else if(s.find(2)==s.end()) cout<<2;
    else cout<<3;
    return 0;
}