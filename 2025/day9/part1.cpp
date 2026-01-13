
#include "../../util.hpp"

struct Point {
    int x,y;
} point;
bool operator==(Point const& p1, Point const& p2) { return (p1.x == p2.x) && (p1.y == p2.y); }
void printPoint(Point& p){ printf("%d-%d", p.x, p.y); }

struct Item{
    Point point1;
    Point point2;
    long long area;
} item;

bool compareItemArea(const Item &a, const Item &b) { return a.area > b.area; }


void printItem(Item& item){ printPoint(item.point1); printf(" "); printPoint(item.point2); printf(" area : %lld\n", item.area);}

int main() {
    // auto lines = readInput("input_small.txt");
    auto lines = readInput("input.txt");   

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
            if (p1.x == p2.x || p1.y == p2.y) { items.emplace_back(Item{p1, p2, 0}); continue; }

            

            long long area = (static_cast<long long>((p2.x-p1.x)+1))*static_cast<long long>((abs(p2.y-p1.y)+1));
            items.emplace_back(Item{p1, p2, area});
        }
    }

    for (auto& item : items){ printItem(item); }
    sort(items.begin(), items.end(), compareItemArea);
    for (auto& item : items){ printItem(item); }
    
    // auto max = *std::max_element(items.begin(),items.end(), [](const Item& a,const Item& b) { return a.area < b.area; });

    printf("Max area : %lld \n", items[0].area);

    return 0;
}

