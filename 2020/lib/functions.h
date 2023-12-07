#ifndef FUNCTIONS_H
#define FUNCTIONS_H
std::unordered_map<std::string, std::string> parseFlags(int argc, char *argv[]);

std::string configToPath(std::unordered_map<std::string, std::string> config);

std::vector<std::string> readFile (std::string fileName);
#endif
