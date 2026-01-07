
#include "../../util.hpp"


int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   

    // for (auto& line : lines){
    //     printf("%s\n", line.c_str());
    // }

    vector<vector<int>> nums;
    vector<string> operations;
    bool operations_input = false;
    for (auto& line : lines) {
        if (line.find('+') < line.length() || line.find('*') < line.length())  { operations_input = true; }    

        string trimmed_line;
        remove_extra_whitespaces(line, trimmed_line);
        // printf("normal:%s\n", line.c_str());
        // printf("trimed:%s\n", trimmed_line.c_str());

        vector<string> split_trimmed = splitString(trimmed_line, ' ');
        // for (auto& s : split_trimmed){
        //     printf("-> s : %s ", s.c_str());
        // }
        // printf("\n");

        if (operations_input) {
            operations = split_trimmed;
        } 
        else {
            vector<int> num_list;
            nums.emplace_back(splitStringInt(trimmed_line, ' '));
        }
    }
    
    // for (auto& line : nums){
    //     for (auto& num : line){
    //         printf("num %d - ", num);
    //     }
    // }
    // printf("\n");

    printf("size : %ld\n", nums.size());       
    printf("size line: %ld\n", nums[0].size());       
    printf("size oper: %ld\n", operations.size());       

    // for (auto& op : operations){
    //     printf("op %s - ", op.c_str());
    // }
    // printf("\n");

    long long totalSum = 0;
    
    for (int line = 0; line < nums[0].size(); line++){
        long long temp_result = 0;

        if (operations[line] == "*"){
            temp_result = 1;
        }
        for (int num_index = 0; num_index < nums.size(); num_index++){
            if (operations[line] == "+"){
                temp_result += nums[num_index][line];
            } else if (operations[line] == "*") {
                temp_result *= nums[num_index][line];
            }
        }
        printf("temp result : %lld\n", temp_result);
        // if (operations[line] == "*"){
        //     temp_result = std::accumulate(vars, end(vars), 1.0, std::multiplies<double>());

        // }
        totalSum += temp_result;
    }
    printf("total sum: %lld\n", totalSum);


    return 0;
}

