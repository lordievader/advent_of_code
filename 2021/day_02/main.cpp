#include <iostream>
#include <vector>
#include <unordered_map>
#include <regex>
#include <cstring>

#include "../lib/functions.h"

using namespace std;

void partOne(vector<string> contents) {
    regex directionRegex ("^([a-z]+) .*");
    regex amountRegex ("^[a-z]+ (.*)");
    cmatch cm;
    string direction;
    uint amount;

    int depth = 0;
    int position = 0;

    for (int i=0; i<(contents.size()); i++){
        int n = contents[i].length();
        char char_array[n+1];
        strcpy(char_array, contents[i].c_str());
        
        // Direction
        regex_match(char_array, cm, directionRegex);
        direction = string(cm[1]);

        // Amount
        regex_match(char_array, cm, amountRegex);
        amount = stoi(cm[1]);

        if (direction == "forward"){
            position += amount;
        }
        else if (direction == "down") {
            depth += amount;
        }
        else if (direction == "up") {
            depth -= amount;
        }
    }
    cout << "Depth: " << depth << endl;
    cout << "Position: " << position << endl;
    cout << "Answer: " << depth * position << endl;
}

void partTwo(vector<string> contents) {
    regex directionRegex ("^([a-z]+) .*");
    regex amountRegex ("^[a-z]+ (.*)");
    cmatch cm;
    string direction;
    uint amount;

    int depth = 0;
    int position = 0;
    int aim = 0;

    for (int i=0; i<(contents.size()); i++){
        int n = contents[i].length();
        char char_array[n+1];
        strcpy(char_array, contents[i].c_str());
        
        // Direction
        regex_match(char_array, cm, directionRegex);
        direction = string(cm[1]);

        // Amount
        regex_match(char_array, cm, amountRegex);
        amount = stoi(cm[1]);
        
        if (direction == "forward"){
            position += amount;
            depth += aim * amount;
        }
        else if (direction == "down") {
            aim += amount;
        }
        else if (direction == "up") {
            aim -= amount;
        }
    }
    cout << "Depth: " << depth << endl;
    cout << "Position: " << position << endl;
    cout << "Answer: " << depth * position << endl;
}

int main(int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    partOne(contents);
    partTwo(contents);
}
