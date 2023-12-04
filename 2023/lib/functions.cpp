#include "functions.h"
#include <fstream>
#include <filesystem>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

template<typename K, typename V>
void print_map(unordered_map<K, V> const &m)
{
    for (auto const &pair: m) {
        cout << "{" << pair.first << ": " << pair.second << "}\n";
    }
}

void print_vector(vector<string> const &v)
{
    for (auto const &item: v) {
        std::cout << "[" << item << "]\n";
    }
}

void print_vectorc(vector<char> const &v)
{
    for (auto const &item: v) {
        std::cout << "[" << item << "]\n";
    }
}

unordered_map<string, string> parseFlags (int argc, char *argv[]) {
    unordered_map<string,string> config;
    config["debug"] = "false";
    config["name"] = "input";
    config["program"] = argv[0];
    int opt;
    string name = "";
    while ((opt = getopt(argc, argv, "d")) != -1) {
        switch (opt) {
            case 'd':
                config["debug"] = "true";
                break;
            default: /* '?' */
                fprintf(stderr, "Usage: %s [-d] name\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    if (optind >= argc) {
        fprintf(stderr, "Expected argument after options\n");
        exit(EXIT_FAILURE);
    }

    config["name"] = argv[optind];
    if (config["debug"] == "true") {
        printf ("Config flags:\n");
        print_map(config);
    }
    return config;
}

std::string configToPath (unordered_map<string, string> config) {
    // Determine path to file
    string path;
    path = filesystem::current_path();
    path += "/" + config["name"];
    path = filesystem::canonical(path);
    if (config["debug"] == "true") {
        cout << "Path to file is " << path << '\n';
    }
    return path;
}

vector<string> readFile (std::string path) {
    // Read file
    string line;
    vector<string> output;
    ifstream inputFile;
    inputFile.open(path);
    if (inputFile.is_open())
    {
        while ( getline (inputFile, line) )
        {
            output.push_back(line);
        }
        inputFile.close();
    }

    else cout << "Unable to open file" << endl;
    return output;
}
