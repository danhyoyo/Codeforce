#include <bits/stdc++.h>
using namespace std;
int main(){
    string s,str=""; cin>>s;
    multiset<char> a;
    for(int i=0;i<s.length();i++){
        if(s[i]>='0'&&s[i]<='9') a.insert(s[i]);
    }
    for(auto it=a.begin();it!=a.end();it++){
        str=str+*it+'+';
    }
    for(int i=0;i<str.length()-1;i++) cout<<str[i];
    return 0;
}