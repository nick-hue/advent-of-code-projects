#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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

std::vector<int> simulateClicking(int dir, int number, int current_point){
    int result_point = (current_point + (dir * number) + 100) % 100;
    int counter = 0;

    for (int i = 1; i <= number; i++){
        int point = current_point + i * dir;
        if (point % 100 == 0){
            counter++;
            printf("point : %d\n", point);
        }
            
    }
    std::vector<int> res = {counter, result_point};
    return res;
}

int main(){
    // std::vector<std::string> inputData = readInput("input_test.txt");
    std::vector<std::string> inputData = readInput("input.txt");

    int point = 50;
    printf("Current point : %d\n", point);
    int counter = 0;
    for (auto &str : inputData){
        // printf("%s \t|\t", str.c_str());
        const char* string_split = str.c_str();
        
        char direction = str.at(0);
        int dir = (direction == 'L') ? -1 : 1;
        // printf("direction : %c |\t", direction);
        // printf("dir int : %d |\t", dir);
        
        std::string number_str = str.substr(1);
        int number = std::stoi(number_str);
        // printf("number : %d", number);

        std::vector<int> res = simulateClicking(dir, number, point);
        counter += res[0];
        point = res[1];
    }
    printf("Counter : %d\n", counter);

    return 0;
}
