#include <iostream>
using namespace std;
int main(){
    int k, r,c=1; cin>>k>>r;
    int a = k;
    while (a%10 != 0 && a%10 != r){
        c+=1;
        a+=k;
    }
    cout<<c;
    return 0;
}