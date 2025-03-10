#include <bits/stdc++.h>
using namespace std;
int n, a[15];
long long S, curMoneySum;
vector <int> curMoneySet;

void printMoneySet()
{
    for (auto i : curMoneySet) cout << a[i] << " ";
    cout << "\n";
}

//Hàm đệ quy
void genMoneySet(int pos)
{
    int lastIndex = (curMoneySet.empty() ? 1 : curMoneySet.back());
    for (int i = lastIndex; i <= n; i ++)
    {
        //Lấy thêm 1 tờ tiền mới vào tập hợp
        curMoneySet.push_back(i);
        curMoneySum += a[i];

        //Gọi đệ quy
        if (curMoneySum >= S)
        {
            if (curMoneySum == S) printMoneySet();
        }
        else genMoneySet(pos + 1);

        //Bỏ tờ tiền này ra khỏi tập hợp
        curMoneySet.pop_back();
        curMoneySum -= a[i];
    }
}

int main()
{
    cin >> n >> S;
    for (int i = 1; i <= n; i ++) cin >> a[i];
    curMoneySet.clear();
    curMoneySum = 0;
    genMoneySet(1);

    return 0;
}