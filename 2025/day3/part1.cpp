#include "../../util.hpp"

int main() {
    auto lines = readInput("input_small.txt");
    // auto lines = readInput("input.txt");

    int sum = 0;

    for (auto& bank : lines){
        printf("bank : %s\n", bank.c_str());
        // std::vector<std::string> splitUp = splitStringIndecesString(bank, 1);
        std::vector<int> splitUp = splitStringIndecesInt(bank, 1);
        std::map<int, int> dataMap = {};
        for (int i = 0; i < splitUp.size(); i++){
            dataMap.insert({i, splitUp[i]});
        }
        
        std::vector<int> keys, values;
        for(std::map<int,int>::iterator it = dataMap.begin(); it != dataMap.end(); ++it) {
            keys.push_back(it->first);
            values.push_back(it->second);
            // std::cout << "Key: " << it->first << " -- Value: " << it->second << std::endl;
        }
        
        // get index of max
        auto index1 = std::distance(values.begin(), std::max_element(values.begin(), values.end()));
        printf("index1 : %ld\n", index1);
        printf("before remove\n");
        for (auto& val : values) { printf("%d ", val); } printf("\n");
                
        values.at(index1) = 0;

        printf("after remove\n");
        for (auto& val : values) { printf("%d ", val); } printf("\n");
        auto index2 = std::distance(values.begin(), std::max_element(values.begin(), values.end()));
        printf("index2 : %ld\n", index2);
        
        int final_num = (index1 < index2) ? std::stoi(std::to_string(dataMap[index1])+std::to_string(dataMap[index2])) 
                                          : std::stoi(std::to_string(dataMap[index2])+std::to_string(dataMap[index1]));
        printf("final num : %d\n\n", final_num);
        sum += final_num;
    }

    printf("Sum is %d\n", sum);


    

    return 0;
}

