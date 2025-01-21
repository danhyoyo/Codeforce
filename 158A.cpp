#include <bits/stdc++.h>
using namespace std;
int main(){
    int a[101],n,k,dem=0; cin>>n>>k;
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    for(int i=1;i<=n;i++){
        if(a[i]>=a[k]&&a[i]>=1) dem++;
    }
    cout<<dem;
    return 0;
}