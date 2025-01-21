#include <bits/stdc++.h>
using namespace std;
string kq(string s){
    int n=s.size();
    if(s[0]=='1'&&s[1]=='0'){
        if((s[2]=='0')||(s[2]=='1'&&n<4)||n<3) return "NO";
        else return "YES";
    } else return "NO";
}
int main(){
    int t; cin>>t;
    while(t--){
        string s; cin>>s;
        cout<<kq(s)<<endl;
    }
    return 0;
}