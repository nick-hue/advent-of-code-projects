makefile_template='CXX=g++
CXXFLAGS=-std=c++20 -O2 -Wall -Wextra -Wshadow -Wconversion

all: part1 part2

part1: part1.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

part2: part2.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f part1 part2
'
print -r -- "$makefile_template" > "$dir_name/Makefile"
