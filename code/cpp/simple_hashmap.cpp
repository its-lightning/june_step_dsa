#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main(){
    unordered_map<string, int> prod_catalog;

    int m;
    cin >> m;
    string x;
    int y;

    for (int i=0 ;i < m; i++){
        cin >> x >> y;
        prod_catalog[x] = y;
    }

    int k, bill = 0;
    cin >> k;

    for (int i = 0; i < k; i++){
        cin >> x >> y;
        bill += prod_catalog[x] * y;
    }
    cout << bill;
}