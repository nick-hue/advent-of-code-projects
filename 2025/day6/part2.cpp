
#include "../../util.hpp"

vector<string> GetCurrentCol(int col_index, vector<vector<string>>& matrix){
    vector<string> result;

    for (int i = 0; i < matrix.size(); i++){ result.emplace_back(matrix[i][col_index]); }   

    return result;
}

bool AllBlank(vector<string> vec){
    return std::adjacent_find( vec.begin(), vec.end(), std::not_equal_to<>() ) == vec.end();
}

int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   

    // vector<vector<string>> nums; 
    vector<string> nums; 
    vector<string> operations;
    bool operations_input = false;
    for (auto& line : lines) {
        if (line.find('+') < line.length() || line.find('*') < line.length())  { operations_input = true; }    

        string trimmed_line;
        remove_extra_whitespaces(line, trimmed_line);

        vector<string> split_trimmed = splitString(trimmed_line, ' ');

        if (operations_input) operations = split_trimmed;
        else {
            // nums.emplace_back(splitString(line, ' '));
            nums.emplace_back(line);
            // nums.emplace_back(vector<string> {"-"});
        }

    }


    printf("size : %ld\n", nums.size());       
    printf("size line: %ld\n", nums[0].size());       
    printf("size oper: %ld\n", operations.size());       
    // format nums

    vector<vector<int>> final_nums;
    vector<int> tmp_ints;
    for (int y = 0; y < nums[0].size(); y++){

        string tmp_string;
        for (int x = 0; x < nums.size(); x++){
            tmp_string += nums[x][y];
            // printf("[%c]", nums[x][y]);
        }
        printf("tmp : [%s]", tmp_string.c_str());
        printf("\n");
        
        // if (tmp_string == "   ") {
        if (tmp_string == "    ") {
            // printf("empty");
            final_nums.emplace_back(tmp_ints);
            tmp_ints = {};
            continue;
        }
        tmp_ints.emplace_back(stoi(tmp_string));
    }
    final_nums.emplace_back(tmp_ints);

    // printf("Operations :\n");
    // for (auto& op : operations){
    //     printf("[%s] ", op.c_str());
    // }
    // printf("\n"); 

    int op_index = 0;
    long long totalSum = 0;
    for (auto& nums : final_nums){
        string op_char = operations[op_index];
        long long tmp_result = op_char == "*" ? 1 : 0;
        for (auto& num : nums){
            printf("%d %s ", num, op_char.c_str());
            if (op_char == "*") tmp_result *= num;
            else if (op_char == "+") tmp_result += num;
            else printf("ERROR\n");
        }
        totalSum += tmp_result;
        op_index++;
        printf("\n");
    }

    printf("final result : %lld\n", totalSum);

    return 0;
}

