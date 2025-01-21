#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    while(t--){
        int n, m; cin>>n>>m;
        vector<pair<int,int>> b[m];
        vector<int> a[n];
        for(int i = 0 ;i <n ; i++){
            for(int j=0;j<m;j++){
                int c;
                cin>>c;
                a[i].push_back(c);
            }
            sort(a[i].begin(), a[i].end());
        }
        for(int i = 0 ;i <n ; i++){
            for(int j=0;j<m;j++){
                b[j].push_back({i, a[i][j]});
            }
        }
        for(int j=0;j<m;j++){
            sort(b[j].begin(), b[j].end(), [](pair<int, int> a, pair<int, int> b) {
                return a.second < b.second; 
            });
        }
        vector<int> st;
        bool check = 1;
        for (auto x:b[0]){
                st.push_back(x.first);
            }
        int l = b[0][n-1].second;
        for(int j=1;j<m;j++){
            vector<int> phu;
            for (auto x:b[j]){
                phu.push_back(x.first);
            }
            if ((phu!=st) || (l>=b[j][0].second)){
                check = 0;
                break;
            }
            l = b[j][n-1].first;
        }
        if(check==1){
            for (auto x:st){
                cout<<x+1<<" ";
            }
            cout<<endl;
        } else cout<<-1<<endl;
    }
    return 0;
}