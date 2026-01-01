
#include "../../util.hpp"


int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    for (auto& line : lines){
        printf("%s\n", line.c_str());
    }

    vector<vector<int>> nums;
    vector<char> operations;
    bool operations_input = false;
    for (auto& line : lines) {
        if (line.find('+') != std::string::npos)  { operations_input = true; continue; }    
        string trimmed_line;
        remove_extra_whitespaces(line, trimmed_line);
        printf("->%s\n", line.c_str());
        printf("->%s\n", trimmed_line.c_str());

        vector<string> str = splitString(trimmed_line, ' ');
        for (auto& s : str){
            printf("-> s : %s", s.c_str());
        }
        printf("\n");

        if (operations_input) {
            nums.emplace_back(splitString(line, ' '));
        } 
        else {
            // make all the numbers of each row into integer vectors
            vector<string> nums_str = splitString(line, ' ');
            vector<int> num_vector;
            std::transform(nums_str.begin(), nums_str.end(), std::back_inserter(num_vector), [](const std::string& str) { return std::stoi(str); });
            operations.emplace_back(num_vector);
        }

        for (auto& op : operations){
            printf("op %c - ", op);
        }

        
        for (auto& line : nums){
            for (auto& num : line){
                printf("num %d - ", num);
            }
        }

    }

    return 0;
}

