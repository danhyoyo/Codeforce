#include <bits/stdc++.h>
using namespace std;
int main(){
    int a[6][6];
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cin>>a[i][j];
            if(a[i][j]!=0){
                cout<<abs(2-i)+abs(2-j);
            }
        }
    }
    return 0;
}