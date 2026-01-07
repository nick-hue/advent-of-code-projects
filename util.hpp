#pragma once
#include <bits/stdc++.h>
using namespace std;

#define MIN(x, y) (x < y ? x : y)
#define MAX(x, y) (x > y ? x : y)

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

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}


std::vector<int> splitStringInt(std::string& input, char delimiter)
{

    // Creating an input string stream from the input string
    std::istringstream stream(input);

    // Vector to store the tokens
    std::vector<int> tokens;

    // Temporary string to store each token
    std::string token;

    // Read tokens from the string stream separated by the
    // delimiter
    while (getline(stream, token, delimiter)) {
        // Add the token to the vector of tokens
        if (!is_number(token)) continue;
        tokens.push_back(stoi(token));
    }

    // Return the vector of tokens
    return tokens;
}

std::vector<std::string> splitStringIndecesString(std::string& input, int index)
{

    // Creating an input string stream from the input string
    std::istringstream stream(input);

    // Vector to store the tokens
    std::vector<std::string> tokens;

    
    // Temporary string to   store each token
    std::string token;

    for (size_t i = 0; i < input.size(); i+=index){
        tokens.push_back(input.substr(i, index));
    }

    // Return the vector of tokens
    return tokens;
}

std::vector<int> splitStringIndecesInt(std::string& input, int index)
{
    // Creating an input string stream from the input string
    std::istringstream stream(input);

    // Vector to store the tokens
    std::vector<int> tokens;
    
    // Temporary string to store each token
    std::string token;

    for (size_t i = 0; i < input.size(); i+=index){
        tokens.push_back(std::stoi(input.substr(i, index)));
    }

    // Return the vector of tokens
    return tokens;
}

int GetIndexByElement(std::vector<int> v, int element){
    return find(v.begin(), v.end(), element) - v.begin();
}

void remove_extra_whitespaces(const string &input, string &output)
{
    output.clear();  // unless you want to add at the end of existing sring...
    unique_copy (input.begin(), input.end(), back_insert_iterator<string>(output),
                                     [](char a,char b){ return isspace(a) && isspace(b);});  
}