#include <iostream>
#include <stdexcept>
#include <vector>
#include <unordered_map>

#include "../lib/functions.h"
#include "day01.h"

using namespace std;

auto main(int argc, char *argv[]) -> int {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    Day01 day01 = Day01(flags, contents);
    try {
        day01.solvePartOne();
        day01.solvePartTwo();
    } catch (const std::out_of_range) {
        cout << "Out of range error" << endl;
        return 1;
    }
    return 0;
}
