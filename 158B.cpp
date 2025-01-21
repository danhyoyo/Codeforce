#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,a[5]={0},sum=0; cin>>n;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        a[x]++;
    }
    sum+=a[4];
    sum+=(int)a[2]/2;
    a[2]=a[2]%2;
    if(a[3]<a[1]){
        sum+=a[3];
        a[1]-=a[3];
        sum+=(int)a[1]/4;
        a[1]=a[1]%4;
    } else{
        sum+=a[3];
        a[1]=0;
    }
    if(a[2]==1){
        sum++;
        if(a[1]>2) sum++;
    } else {if(a[1]>0) sum++;}
    cout<<sum<<endl;
    return 0;
}