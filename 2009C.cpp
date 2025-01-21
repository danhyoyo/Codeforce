#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int x,y,k,i=0; cin>>x>>y>>k;
        bool b=true;
        while(x>0||y>0){
            if(b==true){
                i++;
                x-=k;
                b=false;
            }
            else{
                i++;
                y-=k;
                b=true;
            }
        }
        cout<<i<<endl;
    }
    return 0;
}