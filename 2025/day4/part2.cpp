
#include "../../util.hpp"

bool CanBeAccessed(int x, int y, std::vector<std::string>& lines){ 
    // can be accessed if they are fewer than 4 rolls in the 8 adjecent positions
    int rolls = 0;
    int width = lines[0].size();
    int height = lines.size();
    // printf("grid dims %dx%d\n", width, height);

    for (int i = x - 1; i <= x + 1; i++){
        for (int j = y - 1; j <= y + 1; j++){
            if (i == 0 && j == 0) continue; // no need to check given point
            // check if checking point is out of bounds
            if (i < 0 || j < 0) continue;
            if (i >= width || j >= height) continue;
            
            char cell = lines[i][j];
            // printf("checking point (%d,%d) : %c\n", i, j, cell);
            if (cell == '@' || cell == 'x')  {
                rolls++;
            }
            if (rolls > 4) return false;
        }
    }
    return true;
}

std::vector<std::pair<int, int>> GetRemoveableRolls(std::vector<std::string> lines){
    int counter = 0; 
    std::vector<std::pair<int, int>> points; 

    for (int i = 0; i < lines.size(); i++){
        std::string line = lines[i];
        for (int j = 0; j < line.size(); j++){
            // printf("Current cell : %c at (%d,%d)\n", line[j], i, j);
            if (lines[i][j] == '@' && CanBeAccessed(i, j, lines)){
                counter++;
                points.emplace_back(std::pair<int, int> {i, j});
                // lines[i][j] = 'x';
            }
        }
        // printf("\n");
    }
    return points;
}

void RemoveRolls(std::vector<std::pair<int, int>>rolls, std::vector<std::string>& lines){
    for (auto& pair : rolls){
        lines[pair.first][pair.second] = '.';
    }
}

int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   

    printf("Before\n");
    for (int i = 0; i < lines.size(); i++){
        std::string line = lines[i];
        for (int j = 0; j < line.size(); j++){
            printf("%c", lines[i][j]);
        }
        printf("\n");
    }
    std::vector<std::pair<int, int>> rolls;

    int counter = 0;
    do {
        rolls = GetRemoveableRolls(lines);
        RemoveRolls(rolls, lines);
        counter += rolls.size();
    } while (rolls.size() != 0);

    printf("Total rolls removed : %d\n", counter);
    return 0;
}

