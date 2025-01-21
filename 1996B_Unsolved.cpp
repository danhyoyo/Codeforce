#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        //vector<vector<int>> a;
        int a[1000][1000];
        int n,k; cin>>n>>k;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                //int x; cin>>x;
                //a[i].push_back(x);
                cin>>a[i][j];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cout<<a[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}