#include <iostream>
#include <vector>
#include <unordered_map>

#include "../lib/functions.h"

using namespace std;

void partOne(vector<string> contents) {
    int previous = stoi(contents[0]);
    int current;
    int count = 0;
    for (long unsigned int i=0; i<(contents.size()); i++){
        current = stoi(contents[i]);
        if (current > previous){
            count += 1;
        }
        //printf("%3d %3d|Change in depth: %d\n", previous, current, diff);
        previous = current;
    }
    printf("There were %d increases in depth\n", count);
}

void partTwo(vector<string> contents) {
    int levels[contents.size()];
    for (long unsigned int i=0; i<(contents.size()); i++){
        levels[i] = stoi(contents[i]);
    }

    int previous = levels[0] + levels[1] + levels[2];
    int current;
    int count;
    for (long unsigned int i=1; i<(contents.size()-1); i++){
        current = levels[i-1] + levels[i] + levels[i+1];
        if (current > previous){
            count += 1;
        }
        previous = current;
    }
    printf("There were %d increases in windowed depth\n", count);
}

int main(int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    partOne(contents);
    partTwo(contents);
    return 0;
}
