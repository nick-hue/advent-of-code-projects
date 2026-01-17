
#include "../../util.hpp"

constexpr char LIGHT_DRAGRAM = '[';
constexpr char WIRING = '(';
constexpr char JOLTAGE = '{';

// (0,2,3,4)
vector<int> ParsePart(string& word, char open_char, char close_char){

    word.erase(remove(word.begin(), word.end(), open_char), word.end());
    word.erase(remove(word.begin(), word.end(), close_char), word.end());

    vector<string> split_word = splitString(word, ',');
    vector<int> result;

    transform(split_word.begin(), split_word.end(), back_inserter(result),
            [](string& str) -> int { return stoi(str); });

    return result;
}

void switchBit(int index, string& str){
    str[index] = str[index] == '1'?'0':'1';
}

struct Line
{
    string light_diagram;
    vector<vector<int>> wirings_list;
    vector<int> joltage;
} line ;

void printLine(Line line){
    printf("light diagram => %s\n", line.light_diagram.c_str());
    printf("wirings => ");
    for (auto& el : line.wirings_list){
        for (auto& e : el){ printf("%d,", e); }
        printf(" == ");
    }
    printf("\n");
    printf("joltage => ");
    for (auto& el : line.joltage){
        printf("%d,", el);
        printf(" == ");
    }
    printf("\n");
}

vector<Line> GetPartLines(vector<vector<string>>& split_lines){
    vector<Line> part_lines;
    for (auto& line : split_lines){
        Line part; 
        for (auto& word : line){ 
            // printf("%s - ", word.c_str()); 
            // check if its light diagram
            if (word.find(LIGHT_DRAGRAM) != std::string::npos) { part.light_diagram = word; }
            // check if its wirings
            else if (word.find(WIRING) != std::string::npos) { 
                part.wirings_list.emplace_back(ParsePart(word, '(', ')'));
            }
            else if (word.find(JOLTAGE) != std::string::npos) { 
                part.joltage = ParsePart(word, '{', '}');
            } else {
                printf("ERROR [%s]\n", word.c_str());
            } 
        } 
        // printf("\n");
        part_lines.emplace_back(part);
    }
    return part_lines;
}

int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    vector<vector<string>> split_lines;
    for (auto& line : lines){ split_lines.emplace_back(splitString(line, ' ')); }

    vector<Line> part_lines = GetPartLines(split_lines);
    
    for (auto& l : part_lines){ printLine(l); }



    return 0;
}

