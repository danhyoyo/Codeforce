#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,dem=0; cin>>n;
    while(n>5){
        dem+=n/5;
        n%=5;
    }
    if(n==0) cout<<dem;
    else cout<<dem+1;
    return 0;
}
