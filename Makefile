CXX = g++
CXXFLAGS = -std=c++20 -O2 -Wall -Wextra -Wshadow -Wconversion

all: part1 part2

part1: part1.cpp
	$(CXX) $(CXXFLAGS) -o part1 part1.cpp

part2: part2.cpp
	$(CXX) $(CXXFLAGS) -o part2 part2.cpp

clean:
	rm -f part1 part2
