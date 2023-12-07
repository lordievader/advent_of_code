#include <iostream>
#include <vector>
#include <unordered_map>

#include "../lib/functions.h"

using namespace std;

void partOne (vector<string> contents) {
    for (int i=0; i<(contents.size()); i++){
        int numberA = stoi(contents[i]);
        for (int j=i; j<(contents.size()); j++){
            int numberB = stoi(contents[j]);
            int sum = numberA + numberB;
            if (sum == 2020) {
                int multiplication = numberA * numberB;
                printf(
                    "Number A: %d; Number B: %d; Answer: %d\n",
                    numberA, numberB, multiplication
                );
            }
        }
    }
}

void partTwo (vector<string> contents) {
    for (int i=0; i<(contents.size()); i++){
        int numberA = stoi(contents[i]);
        for (int j=i; j<(contents.size()); j++){
            int numberB = stoi(contents[j]);
            for (int k=j; k<(contents.size()); k++){
                int numberC = stoi(contents[k]);
                int sum = numberA + numberB + numberC;
                if (sum == 2020) {
                    int multiplication = numberA * numberB * numberC;
                    printf(
                        "Number A: %d; Number B: %d; Number C: %d; Answer: %d\n",
                        numberA, numberB, numberC, multiplication
                    );
                }
            }
        }
    }
}

int main (int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    partOne(contents);
    partTwo(contents);
    exit(EXIT_SUCCESS);
}
