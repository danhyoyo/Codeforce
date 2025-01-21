#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        string s; cin>>s;
        if(s.size()%2==1) cout<<"NO"<<endl;
        else{
            string str1="",str2="";
            for(int i=0;i<s.size()/2;i++){
                str1=str1+s[i];
            }
            for(int i=s.size()/2;i<s.size();i++){
                str2=str2+s[i];
            }
            if(str1==str2) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
    }
    return 0;
}