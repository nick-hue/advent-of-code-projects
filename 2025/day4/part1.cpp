
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

    int counter = 0; 
    for (int i = 0; i < lines.size(); i++){
        std::string line = lines[i];
        for (int j = 0; j < line.size(); j++){
            // printf("Current cell : %c at (%d,%d)\n", line[j], i, j);
            if (lines[i][j] == '@' && CanBeAccessed(i, j, lines)){
                counter++;
                lines[i][j] = 'x';
            }
        }
        printf("\n");
    }

    printf("After\n");
    for (int i = 0; i < lines.size(); i++){
        std::string line = lines[i];
        for (int j = 0; j < line.size(); j++){
            printf("%c", lines[i][j]);
        }
        printf("\n");
    }


    printf("Total counter is : %d\n", counter);
    
    return 0;
}

