#include "../../util.hpp"

int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");

    int sum = 0;

    for (auto& bank : lines){
        printf("bank : %s\n", bank.c_str());
        std::vector<int> nums = splitStringIndecesInt(bank, 1);
        std::array<int, 12> indexes = {};
        
        // get index of max
        auto index1 = std::distance(nums.begin(), std::max_element(nums.begin(), nums.end()));
        printf("index1 : %ld\n", index1);
        int num1 = nums[index1];
                
        /* 
            get the second max num in the list:
                -> if its NOT at the end from the point of the first max till the end
                -> if its at the end from the start of the list up to the index of the first max num
        */
        std::ptrdiff_t index2;
        if (index1 == nums.size() - 1) {
            index2 = std::distance(nums.begin(), std::max_element(nums.begin(), nums.end() - 1));
        } else {
            index2 = std::distance(nums.begin(), std::max_element(nums.begin() + index1 + 1, nums.end()));
        }
        int num2 = nums[index2];
        printf("index2 : %ld\n", index2);
        
        int final_num = (index1 < index2) ? std::stoi(std::to_string(num1)+std::to_string(num2)) 
                                          : std::stoi(std::to_string(num2)+std::to_string(num1));

        printf("final num : %d\n\n", final_num);
        sum += final_num;
    }

    printf("Sum is %d\n", sum);


    

    return 0;
}

