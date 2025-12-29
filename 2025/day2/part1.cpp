#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <numeric>
#include <bits/stdc++.h>
#include <iterator>
#include <sstream>

std::vector<std::string> readInput(std::string filename){
    std::fstream file;
    file.open(filename.c_str(), std::ios::in);

    std::string curr_string;
    std::vector<std::string> result;

    while(getline(file, curr_string))
    {
        result.push_back(curr_string) ;
    }

    return result;
}

std::string readInputOneLine(std::string filename){
    std::fstream file;
    file.open(filename.c_str(), std::ios::in);

    std::string curr_string;
    std::vector<std::string> result;

    while(getline(file, curr_string))
    {
        result.push_back(curr_string) ;
    }

    std::string final_string = std::accumulate(result.begin(),result.end(), std::string(""));

    return final_string;
}

std::vector<std::string> splitString(std::string& input, char delimiter)
{

    // Creating an input string stream from the input string
    std::istringstream stream(input);

    // Vector to store the tokens
    std::vector<std::string> tokens;

    // Temporary string to store each token
    std::string token;

    // Read tokens from the string stream separated by the
    // delimiter
    while (getline(stream, token, delimiter)) {
        // Add the token to the vector of tokens
        tokens.push_back(token);
    }

    // Return the vector of tokens
    return tokens;
}

int main(){
    // std::string inputData = readInputOneLine("input_test.txt");
    std::string inputData = readInputOneLine("input.txt");

    // int i = 0;
    // for (auto &data : inputData){
    //     printf("[%d]: %s\n", i++, data.c_str());
    // }
    printf("%s\n", inputData.c_str());

    std::vector<std::string> ranges = splitString(inputData, ',');
    printf("size ranges : %ld\n", ranges.size());
    printf("range : %s\n", ranges[1].c_str());
    std::vector<long long> invalidIds;

    for (auto &range : ranges){
        printf("%s => ", range.c_str());

        std::vector<std::string> splitResult = splitString(range, '-');
        
        std::string start_str = splitResult[0];
        std::string end_str = splitResult[1];
        long long start_ids = std::stoll(start_str);
        long long end_ids = std::stoll(end_str);

        // printf("%d -> %d ", start_ids, end_ids);
        // printf("size of %s : %ld", start_str.c_str(), start_str.size());

        for (long long num = start_ids; num <= end_ids; num++){
            std::string num_str = std::to_string(num);
            // if it cannot be split in the middle it is not invalid
            if (num_str.size() % 2 == 1) continue;

            size_t splitIndex = num_str.size() / 2;
            
            std::string firstPart = num_str.substr(0, splitIndex);
            std::string secondPart = num_str.substr(splitIndex);
            // printf("-->> For the number %s the first is %s, second is %s at index %d", num_str.c_str(), firstPart.c_str(), secondPart.c_str(), splitIndex);            
            // printf("\n");

            if (firstPart == secondPart){
                invalidIds.push_back(num);
            }
            
        }

        // printf("\n");
    }
    printf("\nSum is : %lld\n", std::accumulate(invalidIds.begin(), invalidIds.end(), 0LL));    printf("size : %ld\n", ranges.size());



    return 0;
}
