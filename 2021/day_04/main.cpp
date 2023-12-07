#include <iostream>
#include <unordered_map>
#include <vector>

#include "../lib/functions.h"

using namespace std;

void parseBoard(vector<string> contents){
	// parse number line
	vector<int> numbers;
	string numberLine = contents[0];
	while (numberLine.length() > 1) {
		numbers.push_back(
			stoi(numberLine.substr(0, numberLine.find(",")))
		);
		numberLine.erase(0, numberLine.find(",") + 1);
	}
	numbers.push_back(stoi(numberLine));
	contents.erase(contents.begin(), contents.begin() + 2);

	// parse board 1
	vector<vector<int>> board;
	for (int i = 0; i < 5; i++) {
		numberLine = contents[i];
		cout << numberLine << endl;
		vector<int> boardRow;
		boardRow.push_back(stoi(numberLine.substr(0, numberLine.find(" "))));
		cout << numberLine.substr(0, numberLine.find(" ")) << endl;
	}


}

int main(int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);

	//for (const auto& value: contents) {
	//	std::cout << value << "\n";
	//}
	parseBoard(contents);
}
