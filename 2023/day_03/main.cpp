#include <iostream>
#include <stdexcept>
#include <vector>
#include <unordered_map>

#include "../lib/functions.h"
#include "day.h"

using namespace std;

auto main(int argc, char *argv[]) -> int {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    Day day(flags, contents);
    try {
        day.solvePartOne();
        day.solvePartTwo();
    } catch (const std::out_of_range) {
        cout << "Out of range error" << endl;
        return 1;
    }
    return 0;
}
