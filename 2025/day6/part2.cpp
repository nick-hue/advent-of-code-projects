
#include "../../util.hpp"

vector<string> GetCurrentCol(int col_index, vector<vector<string>>& matrix){
    vector<string> result;

    for (int i = 0; i < matrix.size(); i++){ result.emplace_back(matrix[i][col_index]); }   

    return result;
}

// vector<int> GetColumnNums(vector<string> current_column){
//     vector<int> result; 

//     while (1) {
//         int i = 0;
//         string number_string = "";
//         for (auto& col : current_column){
//             // printf("col : %s\n", col.c_str());
//             if (col == "") {
//                 continue;
//             }
//             number_string += col.back();
//             col.pop_back();
//             i++;
//         }
//         // printf("num str : %s\n", number_string.c_str());
//         if (i == 0) break;
//         result.emplace_back(stoi(number_string));            
//     } 

//     return result;
// }

vector<int> GetColumnNums(vector<string> current_column){
    vector<int> result; 

    // get the max size of a string in the list
    int max_index = distance(current_column.begin(), max_element(current_column.begin(), current_column.end()));
    
    printf("max size index : %d\n", max_index);
    
    for (int ind = 0; ind <= max_index; ind++){
        string number_string;
        for (auto& row : current_column){
            int index = row.size() - (ind + 1);
            if (index < 0) continue;
            printf("doing col : %s\n", row.c_str());
            // printf("row size : %ld\n", row.size());
            printf("getting index %d got num %c\n", index, row[index]);
            
            number_string += row[index];
        }
        result.emplace_back(stoi(number_string));            

    }
        
    return result;
}


int main() {
    auto lines = readInput("input_small.txt");
    // auto lines = readInput("input.txt");   

    // for (auto& line : lines){
    //     printf("%s\n", line.c_str());
    // }

    vector<vector<string>> nums;
    vector<string> operations;
    bool operations_input = false;
    for (auto& line : lines) {
        if (line.find('+') < line.length() || line.find('*') < line.length())  { operations_input = true; }    

        string trimmed_line;
        remove_extra_whitespaces(line, trimmed_line);

        if (operations_input) {
            vector<string> split_trimmed = splitString(trimmed_line, ' ');
            operations = split_trimmed;
        } 
        else {
            nums.emplace_back(splitString(trimmed_line, ' '));
        } 
    }
    
    for (auto& line : nums){
        for (auto& num : line){
            printf("num %s - ", num.c_str());
        }
        printf("\n");
    }
    printf("\n");

    printf("size : %ld\n", nums.size());       
    printf("size line: %ld\n", nums[0].size());       
    printf("size oper: %ld\n", operations.size());       

    // for (auto& op : operations){
    //     printf("op %s - ", op.c_str());
    // }
    // printf("\n");

    long long totalSum = 0;
    
    for (int col = 0; col <= nums.size(); col++){
        vector<string> current_column = GetCurrentCol(col, nums);
        // printf("col index %d\n", col);
        // for (auto& c : current_column){
        //     printf("%s - \n", c.c_str());
        // }
        // printf("\n");

        vector<int> column_nums = GetColumnNums(current_column);
        printf("col index %d\n", col);
        for (auto& n : column_nums){
            printf("%d - \n", n);
        }
        printf("\n");
        
    }

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

