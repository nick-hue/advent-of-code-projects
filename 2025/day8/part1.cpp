
#include "../../util.hpp"

struct Vector3 {
    int x, y, z;
} v3 ;

struct Circuit {
    vector<Vector3> boxes;
} circ ;

bool operator==(Vector3 const& v1, Vector3 const& v2) { return (v1.x == v2.x) && (v1.y == v2.y) && (v1.z == v2.z); }
int GetDistance(Vector3 const& v1, Vector3 const& v2) { return sqrt(pow(v1.x-v2.x, 2)+pow(v1.y-v2.y, 2)+pow(v1.z-v2.z, 2)); }

void printv(Vector3 v){
    printf("x=%d,y=%d,z=%d\n", v.x, v.y, v.z);
}

int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    vector<Vector3> nums;
    transform(lines.begin(), lines.end(), back_inserter(nums),
            [](string& str) -> Vector3 {
                auto split = splitString(str, ',');
                return Vector3{ stoi(split[0]), stoi(split[1]), stoi(split[2]) };
            }
        );
    
    vector<Circuit> circuits = {Circuit{}}; 
    circuits[0].boxes.emplace_back(nums[0]);
    
    // for (auto& cir : circuits[0].boxes){
    //     printv(cir);
    // }
    

    for (const auto& v_start : nums) {
        for (const auto& v_check : nums) {
            if (v_start == v_check) continue;

            int dist = GetDistance(v_start, v_check);
            printv(v_start);
            printv(v_check);
            printf("distance between: %d\n", dist);
            
        }

        break;
    }

    

    return 0;
}

