#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        cin.ignore();
        string s[n];
        for(int i=0;i<n;i++){
            cin>>s[i];
        }
        for(int i=n-1;i>=0;i--){
            cout<<s[i].find('#')+1<<" ";
        }
        cout<<endl;
    }
    return 0;
}