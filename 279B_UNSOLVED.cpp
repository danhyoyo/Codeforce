#include <bits/stdc++.h>
using namespace std;
int main(){
    int t, n,j=0,maxx=-1; cin>>n>>t;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        int x; cin>>x;
        a.push_back(x);
    }
    for(int i=0;i<n;i++){
        int j=i,dem=0,x=t;
        while(j<n&&(x-a[j])>=0){
            dem++;
            x-=a[j];
            j++;
        }
        if(maxx<dem) maxx=dem;
    }
    cout<<maxx;
    return 0;
}