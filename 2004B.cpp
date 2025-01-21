#include <bits/stdc++.h>
using namespace std;
signed main(){
    // freopen("input.inp","r",stdin);
    // freopen("output.out","w",stdout);
    int t; cin>>t;
    while(t--){
        int l,r,L,R,kq; cin>>l>>r>>L>>R;
        if(l>L){
            swap(l,L);
            swap(r,R);
        } else if (l==L){
            if(r-l>R-L){
                swap(R,r);
                swap(l,L);
            }
        }
        if(L-r>=1) kq=1;
        else if(r==R&&l==L){
            kq=R-L;
        } else if(R>r&&L==l){
            kq=r-l+1;
        } else if(R>r){
            kq=r-L+2;
        } else if(r>R){
            kq=R-L+2;
        } else if(r==R){
            kq=R-L+1;
        }
        cout<<kq<<endl;
    }
    return 0;
}