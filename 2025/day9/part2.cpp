
#include "../../util.hpp"

struct Item{
    Point point1;
    Point point2;
    long long area;
} item;

bool compareItemArea(const Item &a, const Item &b) { return a.area > b.area; }

bool IsRedTile(int x, int y, vector<Point>& points){
    for (auto& p : points){ if (x == p.x && y == p.y) return true; }
    return false;
}

bool IsGreenTile(int x, int y, vector<Point>& points){
    for (auto& p : points){ if ((x != p.x && y == p.y) || (x == p.x && y != p.y)) return true; }
    return false;
}

void DrawMap(int width, int height, vector<Point>& points){
    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
            if (IsRedTile(x, y, points)) { printf("#"); continue; }
            if (IsGreenTile(x, y, points)) { printf("X"); continue; };
            printf(".");
        }
        printf("\n");
    }
}


int main() {
    auto lines = readInput("input_small.txt");
    //auto lines = readInput("input.txt");   

    vector<Point> points;
    transform(lines.begin(), lines.end(), back_inserter(points),
            [](string& str) -> Point {
                auto split = splitString(str, ',');
                return Point { stoi(split[0]), stoi(split[1]) };
            }
        );

    vector<Item> items;
    for (auto& p1 : points){
        for (auto& p2 : points){
            if (p1 == p2) continue;           

            long long area = (static_cast<long long>((p2.x-p1.x)+1))*static_cast<long long>((abs(p2.y-p1.y)+1));
            items.emplace_back(Item{p1, p2, area});
        }
    }

    DrawMap(14, 9, points);

    return 0;
}

