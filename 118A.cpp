#include <bits/stdc++.h>
using namespace std;
int main(){
    //"A", "O", "Y", "E", "U", "I"
    string s; cin>>s;
    int n = s.size();
    for(int i=0;i<n;i++){
        s[i]=tolower(s[i]);
    }
    for(int i=0;i<n;i++){
        if(s[i] == 'a' || s[i] == 'o' || s[i] == 'y' || s[i] == 'e' || s[i] == 'u' || s[i] == 'i'){
            continue;
        } else cout<<'.'<<s[i];
    }
    return 0;
}