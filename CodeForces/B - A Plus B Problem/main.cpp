#include <bits/stdc++.h>
using namespace std;

int rows[3][1000000];
int n, q;
int r, c, d;

void print() {
    for (int i = 0;i < 3;i++) {
        for(int j = 0;j < n;j++) {
            printf("%d ", rows[i][j]);
        }
        printf("\n");
    }
}

int main() {
    std::cin >> n >> q;
    int first, second;
    std::cin >> first >> second;
    for (int j = n - 1;j > -1;j--) {
        rows[0][j] = first%10;
        first /= 10;
    }
    for (int j = n - 1;j > -1;j--) {
        rows[1][j] = second%10;
        second /= 10;
    }
    int pointer = n - 1;
    int sum = rows[0][pointer] + rows[1][pointer];
    while(pointer >= 0) {
        rows[2][pointer] = sum%10;
        sum /= 10;
        pointer--;
        sum += (rows[0][pointer] + rows[1][pointer]);
    }
    rows[2][pointer] = sum%10;
    for (int i = 0; i < q;i++) {
        // print();
        std::cin >> r >> c >> d;
        r -= 1;
        c -= 1;
        int changed = 0;
        int sum = 0;
        int pointer = c;
        if (rows[r][c] != d) {
            changed++;
            rows[r][c] = d;
            int pointer = n - 1;
            int sum = rows[0][pointer] + rows[1][pointer];
            while(pointer >= 0) {
                if (rows[2][pointer] != sum%10) {
                    changed++;
                    rows[2][pointer] = sum%10;
                }
                sum /= 10;
                pointer--;
                sum += (rows[0][pointer] + rows[1][pointer]);
            }
            if (rows[2][pointer] != sum%10) {
                changed++;
                rows[2][pointer] = sum%10;
            }
            // print();
        }
        printf("%d %d\n", rows[2][c], changed);
    }
    return 0;
}