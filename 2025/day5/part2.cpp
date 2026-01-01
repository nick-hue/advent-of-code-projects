
#include "../../util.hpp"

int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   

    vector<pair<long long, long long>> ranges;
    vector<long long> ingredients;
    bool ingredient_input = false;
    for (auto& line : lines) {
        if (line.empty()) { break; }
        vector<string> line_split = splitString(line, '-');
        ranges.emplace_back(std::pair<long long, long long> {stoll(line_split[0]), stoll(line_split[1])});
    }

    sort(ranges.begin(), ranges.end());
    
    std::vector<pair<long long,long long>> result_ranges;
    // make range structure from all the range input for better calculations
    for (auto& range : ranges){
        if (result_ranges.size() == 0) {
            result_ranges.emplace_back(range); 
            continue;
        }
        
        bool outsideAll = true;
        for (auto& res_range : result_ranges) {
            // outside the current range checking -> go to next range
            if (range.second < res_range.first || range.first > res_range.second ) { continue; }
            // inside the current range checking -> break
            if (range.first >= res_range.first && range.second <= res_range.second ) {
                outsideAll = false;
                break;
            }
            // half inside (front) -> change the range front side 
            if (range.first < res_range.first && range.second <= res_range.second ) {
                outsideAll = false;
                res_range.first = range.first;
                continue;
            }
            // half inside (back) -> change the range back side 
            if (range.first >= res_range.first && range.second > res_range.second ) {
                outsideAll = false;
                res_range.second = range.second;
                continue;
            }

        }
        // if outside all ranges make a new one 
        if (outsideAll) {
            // printf("new range : %lld-%lld\n", range.first, range.second);
            result_ranges.emplace_back(range);
        }

    }

    long long ids = 0;
    for (auto& range : result_ranges){
        printf("range : %lld-%lld\n", range.first, range.second);
        ids += range.second - range.first + 1;
    }
    
    printf("Num of ids : %lld\n", ids);

    return 0;
}

