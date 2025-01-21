#include <bits/stdc++.h>
using namespace std;
bool check(int a){
    while(a>0){
        if(!(a%10==4||a%10==7)){
            return false;
        }
        a/=10;
    }
    return true;
}
int main(){
    int n; cin>>n;
    for(int i=4;i<=n;i++){
        if(n%i==0){
            if(check(i)){
                cout<<"YES";
                return 0;
            }
        }
    }
    cout<<"NO";
    return 0;
}