#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,sum_x=0,sum_y=0,sum_z=0; cin>>n;
    for(int i=0;i<n;i++){
        int x,y,z; cin>>x>>y>>z;
        sum_x+=x;
        sum_y+=y;
        sum_z+=z;
    }
    if(sum_x==0&&sum_y==0&&sum_z==0) cout<<"YES";
    else cout<<"NO";
    return 0;
}