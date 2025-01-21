#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n,dem=0; cin>>n;
        dem+=n/4;
        n%=4;
        dem+=n/2;
        cout<<dem<<endl;
    }
    return 0;
}