#pragma once
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

template<typename K, typename V>
void print_map(unordered_map<K, V> const &m);
void print_vector(vector<string> const &v);
void print_vectorc(vector<char> const &v);

unordered_map<string, string> parseFlags(int argc, char *argv[]);

string configToPath(unordered_map<string, string> config);

vector<string> readFile (string fileName);
