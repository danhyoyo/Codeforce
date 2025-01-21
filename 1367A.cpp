#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        string s; cin>>s;
        cout<<s[0];
        for(int i=2;i<s.size();i+=2){
            cout<<s[i];
        }
        cout<<s[s.length()-1]<<endl;
    }
    return 0;
}