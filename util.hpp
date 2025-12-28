#pragma once
#include <bits/stdc++.h>
using namespace std;

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
