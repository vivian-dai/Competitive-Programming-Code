#include <bits/stdc++.h>
using namespace std;

int t, n, m, k;

int main() {
    std::cin >> t;
    for (int i = 0;i < t;i++) {
        std::cin >> n >> m >> k;
        if (n*m - 1 == k) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}