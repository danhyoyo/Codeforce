#include <bits/stdc++.h>
using namespace std;
signed main(){
    int t; cin>>t;
    while (t--){
        int a1,a2,b1,b2,dem=0; cin>>a1>>a2>>b1>>b2;
        if((a1>=b1&&a2>b2)||(a1>b1&&a2>=b2)) dem+=2;
        if((a2>=b1&&a1>b2)||(a2>b1&&a1>=b2)) dem+=2;
        cout<<dem<<endl;
    }
    return 0;
}