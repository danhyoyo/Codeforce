#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,sum=0; cin>>n;
    while(n--){
        string s; cin>>s;
        if(s[0]=='+'||s[2]=='+') sum++;
        else if(s[0]=='-'||s[2]=='-') sum--;
    }
    cout<<sum;
    return 0;
}