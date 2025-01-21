#include <bits/stdc++.h>
using namespace std;
int main(){
    string s,str=""; cin>>s;
    int l=s.length(),dem=0;
    for(int i=l-1;i>=0;i++){
        str=s[i]+str;
        if(s.find(str)!=string::npos) dem++;
    }
    cout<<dem;
    //sai bet
    return 0;
}