#include <iostream>
#include <vector>
#include <unordered_map>
#include <regex>
#include <cstring>

#include "../lib/functions.h"

using namespace std;

template<typename K>
void print_vector(vector<K> const &m){
    for (vector<string>::const_iterator i = m.begin(); i != m.end(); i++)
    {
        cout << *i << ' ' << endl;
    }
}

template<typename K>
void partOne(vector<K> const &contents) {
    //print_vector(contents);
    string minCountRegex = "^([0-9]+)-.*";
    string maxCountRegex = "^[0-9]+-([0-9]+).*";
    string characterRegex = "^[0-9]+-[0-9]+ ([a-z]).*";
    string lineRegex = "^[0-9]+-[0-9]+ [a-z]: (.*)";
    int minCount;
    int maxCount;
    string character;
    string line;

    for (int i = 0; i < contents.size(); i++)
    {
        cout << "Line number: " << i << endl;
        cout << contents[i] << endl;
        int n = contents[i].length();
        char char_array[n + 1];
        std::cmatch cm;
        strcpy(char_array, contents[i].c_str());

        // minCount match
        regex minCountExpression (minCountRegex);
        regex_match(char_array, cm, minCountExpression);
        minCount = stoi(cm[1]);
        cout << minCount << endl;
        
        // maxCount match
        regex maxCountExpression (maxCountRegex);
        regex_match(char_array, cm, maxCountExpression);
        maxCount = stoi(cm[1]);
        cout << maxCount << endl;
        
        // character match
        regex characterExpression (characterRegex);
        regex_match(char_array, cm, characterExpression);
        character = string(cm[1]);
        cout << character << endl;
        
        // line match
        regex lineExpression (lineRegex);
        regex_match(char_array, cm, lineExpression);
        line = string(cm[1]);
        cout << line << endl;


        cout << endl;
    }

}

int main (int argc, char *argv[]) {
    unordered_map<string, string> flags = parseFlags(argc, argv);
    string path = configToPath(flags);
    vector<string> contents = readFile(path);
    partOne(contents);
    exit(EXIT_SUCCESS);
}
