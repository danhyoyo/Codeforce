#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin>>s;
    int thuong=0;
    for(int i=0;i<s.size();i++)
        if((s[i]>='a')&&(s[i]<='z'))
            thuong++;
    if(thuong>=s.length()-thuong)
        for(int i=0;i<s.size();i++)
            cout<<(char)tolower(s[i]);
    else
        for(int i=0;i<s.size();i++)
            cout<<(char)toupper(s[i]);
    return 0;
}