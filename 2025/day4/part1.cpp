
#include "../../util.hpp"

int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    for (auto& line : lines){
        printf("%s
", line.c_str());
    }

    return 0;
}

