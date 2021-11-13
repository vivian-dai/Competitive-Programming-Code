#include <bits/stdc++.h>
using namespace std;

int n;
int total = 0;
int p, v, t;
int main() {
    std::cin >> n;
    for (int i = 0;i < n;i++) {
        std::cin >> p >> v >> t;
        if (p + v + t > 1) {
            total++;
        }
    }
    printf("%d", total);
}