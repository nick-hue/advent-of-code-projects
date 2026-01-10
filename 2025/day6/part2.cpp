
#include "../../util.hpp"

vector<string> GetCurrentCol(int col_index, vector<vector<string>>& matrix){
    vector<string> result;

    for (int i = 0; i < matrix.size(); i++){ result.emplace_back(matrix[i][col_index]); }   

    return result;
}

int main() {
    auto lines = readInput("input_small.txt");
    // auto lines = readInput("input.txt");   

    vector<vector<string>> nums; 
    vector<string> operations;
    bool operations_input = false;
    for (auto& line : lines) {
        if (line.find('+') < line.length() || line.find('*') < line.length())  { operations_input = true; }    

        string trimmed_line;
        remove_extra_whitespaces(line, trimmed_line);

        vector<string> split_trimmed = splitString(trimmed_line, ' ');

        if (operations_input) operations = split_trimmed;
        else {
            nums.emplace_back(splitString(line, ' '));
            nums.emplace_back(vector<string> {"-"});
        }

    }

    // format nums
    vector<vector<string>> final_nums;
    for (auto& line : nums){
        vector<string> row;
        int i = 0;
        for (auto& num : line){
            printf("[%s] ", num.c_str());
            if (num == "") continue;
            if (is_number(line[i+1])) row.emplace_back(num);
            if (line[i+1].empty()) row;
            // AB.insert(AB.end(), B.begin(), B.end());
            i++;
        }
        printf("\n");
    }
    printf("\n");

    printf("size : %ld\n", nums.size());       
    printf("size line: %ld\n", nums[0].size());       
    printf("size oper: %ld\n", operations.size());       

    // printf("Operations :\n");
    // for (auto& op : operations){
    //     printf("[%s] ", op.c_str());
    // }
    // printf("\n"); 

    // // long long totalSum = 0;
    
    // for (int col = 0; col <= nums.size(); col++){
    //     vector<string> current_column = GetCurrentCol(col, nums);
    //     // printf("col index %d\n", col);
    //     for (auto& c : current_column){
    //         printf("%s - ", c.c_str());
    //     }
    //     printf("\n");
    // }
    //     vector<int> column_nums = GetColumnNums(current_column);
    //     printf("col index %d\n", col);
    //     for (auto& n : column_nums){
    //         printf("%d - \n", n);
    //     }
    //     printf("\n");
        
    // }

    // for (int line = 0; line < nums[0].size(); line++){
    //     long long temp_result = 0;
    //     if (operations[line] == "*"){
    //         temp_result = 1;
    //     }



    //     totalSum += temp_result;
    // }
    // printf("total sum: %lld\n", totalSum);


    return 0;
}

