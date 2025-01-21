#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int a,b,n,i=0; cin>>a>>b>>n;
        if(a<b){
            a+=b;
            b=a-b;
            a=a-b;
        }
        while(a<=n){
            b+=a;
            a+=b;
            b=a-b;
            a=a-b;
            i++;
        }
        cout<<i<<endl;
    }
    return 0;
}