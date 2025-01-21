#include <bits/stdc++.h>
using namespace std;
int main(){
    int n, m, a, b, sum=0; cin>>n>>m>>a>>b;
    if(a*m<=b){
        sum=a*n;
    } else if(a*m>b){
        sum=(b*((int)(n/m)))+min(b,a*(n%m));
    }
    cout<<sum;
    return 0;
}