
#include "../../util.hpp"


int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   
    
    int startIndex = lines[0].find('S');
    printf("start : %d\n", startIndex);

    // contains all the indexes where the beam is on the board
    set<int> beamIndexes = {startIndex};
    int lineIndex = 0;
    int splitCount = 0;
    for (auto& line : lines){
        set<int> newBeamIndexes;
        vector<int> splitterIndeces = findIndexesOfElement(line, '^');
    
        if (splitterIndeces.size() > 0){
            printf("Splitters found at line with index [%d]: ", lineIndex);
            for (auto& ind : splitterIndeces){ printf("%d ", ind); } printf("\n");
        }
 
        printf("Current Beam Indexes - line : %d\n", lineIndex);
        for (auto& ind : beamIndexes){ 
            printf("%d ", ind); 

            // Check if the current beam index hits a splitter
            int cnt = count(splitterIndeces.begin(), splitterIndeces.end(), ind);
            if (cnt > 0){
                newBeamIndexes.insert(ind-1);
                newBeamIndexes.insert(ind+1);
                splitCount++;
            }
        }
        printf("\n");
        
        // find all the spots where a splitter is
        if (newBeamIndexes.size() > 0)
            beamIndexes = newBeamIndexes;  
        lineIndex++;
    }
    printf("Split counter : %d\n", splitCount);

    

    return 0;
}

