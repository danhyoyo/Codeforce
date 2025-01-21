#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,dem=1; cin>>n;
    cin.ignore();
    string s; cin>>s;
    for(int i=1;i<n;i++){
        if(s[i]!=s[i-1]) dem++;
    }
    cout<<n-dem;
    return 0;
}