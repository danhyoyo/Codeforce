#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    bool b=true;
    for (int i=1;i<s.size();i++){
        if(s[i]>'Z') b=false;
    }
    if(!b) cout<<s;
    else{
        for(int i=1;i<s.size();i++){
            s[i]=tolower(s[i]);
        }
        if(s[0]>'Z') s[0]=toupper(s[0]);
        else s[0]=tolower(s[0]);
        cout<<s;
    }
 
    return 0;
}