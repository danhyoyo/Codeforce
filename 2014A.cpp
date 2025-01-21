#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n,k,a[51],count=0,gold=0; cin>>n>>k;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            if(x>=k) gold+=x;
            if(x==0&&gold!=0){
                gold--;
                count++;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}