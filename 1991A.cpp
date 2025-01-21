#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n,maxle=0,a[101]; cin>>n;
        for(int i=1;i<=n;i++){
            cin>>a[i];
            if(i%2==1&&a[i]>maxle) maxle=a[i]; 
        }
        cout<<maxle<<endl;
    }
    return 0;
}