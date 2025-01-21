#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,a[101],sum=0,sum2=0; cin>>n;
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    sort(a,a+n,greater<int>());
    int i=0;
    while(sum2<=sum-sum2){
        sum2+=a[i];
        i++;
    }
    cout<<i;
    return 0;
}