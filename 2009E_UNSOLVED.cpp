#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        long long n,k,min=INT_MAX; cin>>n>>k;
       // cout<<(k+k+n-1)*n/2;
        for(int i=k+n-1;i>=k;i--){
            long long x=abs((long long)((i+k+n-1)*(k+n-i)/2)-((k+i-1)*(i-k)/2));
            if(min>x) min=x;
        }
        cout<<min<<endl;
    }
    return 0;
}