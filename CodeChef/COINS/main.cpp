#include <bits/stdc++.h>
using namespace std;

int n;

int dp(int n) {
    if (n < 7) {
        return n;
    }
    return max(n, dp(n/2) + dp(n/4) + dp(n/3));
}

int main() {
    for (int i = 0; i < 10; i++) {
        std::cin >> n;
        printf("%d\n", dp(n));
    }
    return 0;
}