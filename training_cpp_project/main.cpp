#include <iostream>
#include <vector>

void Pididi(int n, int m) {
    std::string sp[n + 2][m + 2];
    int total = 0;
    for (int i = 0; i < n + 3; i++) {
        for (int j = 0; j < m + 3; j++) {
            if (i == 0 || j == 0 || i == n + 2 || j == m + 2) {
                sp[i][j] = "1";
            }
        }
    }
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < m + 1; j++) {
            std::string a;
            std::cin >> a;
            sp[i][j] = a;
        }
    }

}


int main() {
    int n, m;
    std::cout << "ФИЛИПП КИРКОРОВ";
    std::cin >> n >> m;
    Pididi(n, m);
    return 0;
}
