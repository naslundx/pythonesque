#include <iostream>

auto print(int i) {
    if (i > 3) {
        while (i > 0) {
            std::cout << i << " ";
            i -= 1;
        }

        std::cout << "\n";
    }
}


int main() {
    auto x = 0;
    auto y = 10;

    while (x < y) {
        x += 1;
        print(x);
    }


}
