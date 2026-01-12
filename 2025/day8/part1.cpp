
#include "../../util.hpp"

struct Vector3 {
    int x, y, z;
} vector3 ;

void printv(Vector3 v){
    printf("%d-%d-%d\n", v.x, v.y, v.z);
}

int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    vector<Vector3> nums;
    transform(lines.begin(), lines.end(), back_inserter(nums), [](string& str) { auto split = splitString(str, ','); return Vector3{stoi(split[0]), stoi(split[1]), stoi(split[3]) });
    for (int i = 0; i < nums.size(); i++){
            
    }


    

    return 0;
}

