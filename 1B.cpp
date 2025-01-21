#include <bits/stdc++.h>
using namespace std;
int base26_10 (string s){
    int n=0,i=s.size()-1;
    for(int i=s.size()-1;i>=0;i--){
        n=n+(s[i]-'A'+1)*pow(26,s.size()-1-i);
    }
    return n;
}
string base10_26 (int n){
    string s;
    while(n>0){
        int x;
        n--;
        x=n%26;
        s =(char)(x+'A') + s;
        n/=26;
    }
    return s;
}
void rxcy(string s){
    int so=0,so2=0,i=1;
    while(s[i]>='0'&&s[i]<='9'){
        so*=10;
        so+=(s[i])-48;
        i++;
    }
    i++;
    while(i<s.size()){
        so2*=10;
        so2+=(s[i])-48;
        i++;
    }
    cout<<base10_26(so2)<<so<<endl;
}
void aa(string s){
    int i=0;
    string xau="";
    while(s[i]>='A'&&s[i]<='Z'){
        xau+=s[i];
        i++;
    }
    cout<<"R";
    while(i<s.size()){
        cout<<s[i];
        i++;
    }
    cout<<"C";
    cout<<base26_10(xau)<<endl;
}
int main(){
    int n; cin>>n;
    while(n--){
        string s; cin>>s;
        int dem=0;
        for(int i=1;i<s.length();i++){
            if((s[i]>='0'&&s[i]<='9')&&(s[i-1]>='A'&&s[i-1]<='Z')) dem++;
        }
        if(dem==2) rxcy(s);
        else aa(s);
    }
    return 0;
}