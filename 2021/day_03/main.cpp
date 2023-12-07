#include <iostream>
#include <vector>
#include <unordered_map>
#include <regex>
#include <cstring>
#include <stdlib.h>
#include <bitset>

#include "../lib/functions.h"

using namespace std;

void partOne(vector<string> contents) {
    string line = contents[0];
    int x = contents.size();
    int y = line.length(); 
    char buffer[x][y];

    // Convert to buffer x,y
    for (int i=0; i<(contents.size()); i++){
        line = contents[i];
        strcpy(buffer[i], line.c_str());
    }

    // Figure out which column contains more
    char gamma[y];
    char epsilon[y];
    for (int j=0; j<y; j++){
        int one = 0;
        int zero = 0;
        for (int i=0; i<x; i++){
            if (buffer[i][j] == '0') {
                zero += 1;
            } else {
                one += 1;
            }
        }
        if (zero > one){
            gamma[j] = '0';
            epsilon[j] = '1';
        } else {
            gamma[j] = '1';
            epsilon[j] = '0';
        }
    }

    string gamma_string = string(gamma);
    string epsilon_string = string(epsilon);
    int gamma_power = stoi(gamma_string, 0, 2);
    int epsilon_power = stoi(epsilon_string, 0, 2);
    cout << "Gamma: " << gamma_power << ", epsilon: " << epsilon_power << endl;
    cout << "Answer: " << gamma_power * epsilon_power << endl;
}

void partTwo(vector<string> contents) {
	int stringLength = contents[0].length();
	std::vector<string> workingSet = contents;
	std::map<int, std::vector<string>> m;
	m[0].clear();
	m[1].clear();

	// Determine the oxygen generator rating
	int charIndex = 0;
	while (workingSet.size() > 1) {
		for (int i = 0; i < workingSet.size(); i++) {
			string line = workingSet[i];
			int bit = (int)line[charIndex] - 48;
			m[bit].push_back(line);
		}
		if (m[0].size() > m[1].size()) {
			workingSet = m[0];
		} else {
			workingSet = m[1];
		}
		m[0].clear();
		m[1].clear();
		charIndex = (charIndex + 1) % stringLength;
	}
	int oxygenGeneratorRating = stoi(workingSet[0], 0, 2);
	cout << "Oxygen generator rating: " << oxygenGeneratorRating << endl;

	// Determine the CO2 scrubber rating
	workingSet = contents;
	m[0].clear();
	m[1].clear();
	charIndex = 0;
	while (workingSet.size() > 1) {
		for (int i = 0; i < workingSet.size(); i++) {
			string line = workingSet[i];
			int bit = (int)line[charIndex] - 48;
			m[bit].push_back(line);
		}
		if (m[0].size() > m[1].size()) {
			workingSet = m[1];
		} else {
			workingSet = m[0];
		}
		m[0].clear();
		m[1].clear();
		charIndex = (charIndex + 1) % stringLength;
	}
	int co2ScrubberRating = stoi(workingSet[0], 0, 2);
	cout << "CO2 scrubber rating: " << co2ScrubberRating << endl;

	int lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating;
	cout << "Life support rating: " << lifeSupportRating << endl;
}


int main(int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);

    partOne(contents);
    partTwo(contents);
}
