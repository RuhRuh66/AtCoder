#include <iostream>

void greet(const char* name) {
    std::cout << "Hello, " << name << std::endl;
}

int main() {
    int nums[3] = {1, 2, 3};
    for (int i = 0; i <= 3; i++) {
        std::cout << "nums[" << i << "] = " << nums[i] << std::endl;
    }

    greet(nullptr);

    return 0;
}
