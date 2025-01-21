#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,sum=0; cin>>n;
    while(n--){
        int a[3],dem=0; cin>>a[0]>>a[1]>>a[2];
        for(int i=0;i<3;i++){
            if(a[i]==1) dem++;
        }
        if(dem<=1) continue;
        else sum++;
    }
    cout<<sum;
    return 0;
}