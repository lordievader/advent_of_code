#include "day.h"
#include "../lib/functions.h"
#include <cstdint>
#include <stdexcept>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

Day::Day(unordered_map<string, string> flags, vector<string> contents)
: _flags(std::move(flags))
, _contents(std::move(contents))
{
}

auto Day::solvePartOne() -> void
{
	int answer = 0;
	for (auto const& line: _contents) {
		Game game(line);
		if (game.isValid()) {
			answer += game.getId();
		}
	}
	cout << "Answer part one: " << answer << endl;
}

auto Day::solvePartTwo() -> void
{
	int answer = 0;
	for (auto const& line: _contents) {
		Game game(line);
		int blue = game.fewestBlues();
		int red = game.fewestReds();
		int green = game.fewestGreens();
		int power = blue * red * green;
		answer += power;
	}
	cout << "Answer part two: " << answer << endl;
}

GameSet::GameSet(string line)
: _line(std::move(line))
{
}

auto operator<<(ostream& stream, GameSet& gameSet) -> ostream&
{
	stream << "Game ID " << gameSet.getLine() << endl;
	return stream;
}

auto GameSet::countBlue() -> int
{
	smatch match;
	int count = 0;
	if(regex_search(_line, match, _blueRegex) && !match.empty()) {
		count = stoi(match.str(1));
	}
	return count;
}

auto GameSet::countRed() -> int
{
	smatch match;
	int count = 0;
	if(regex_search(_line, match, _redRegex) && !match.empty()) {
		count = stoi(match.str(1));
	}
	return count;
}

auto GameSet::countGreen() -> int
{
	smatch match;
	int count = 0;
	if(regex_search(_line, match, _greenRegex) && !match.empty()) {
		count = stoi(match.str(1));
	}
	return count;
}

auto GameSet::isValid() -> bool
{
	const int maxRed = 12;
	const int maxGreen = 13;
	const int maxBlue = 14;
	return countRed() <= maxRed &&
		countGreen() <= maxGreen &&
		countBlue() <= maxBlue;
}

Game::Game(string line)
: _line(std::move(line))
{
	this->parseLine();
	this->parseSets();
}

auto operator<<(ostream& stream, Game& game) -> ostream&
{
	stream << "Game ID " << game.getId() << ", number of sets: " << game.numberOfSets()<< endl;
	return stream;
}

auto Game::parseLine() -> void
{
	smatch match;
	if(regex_search(_line, match, _idRegex) && !match.empty()){
		_id = stoi(match.str(1));
	} else {
		throw std::runtime_error("Id not found in string.");
	}
}

auto Game::parseSets() -> void
{
	size_t index = _line.find(':');
	if (index == string::npos) {
		throw runtime_error("':' of 'Game <id>:' not found");
	}

	size_t start = 0;
	while(index != string::npos){
		start = index + 1;
		index = _line.find(';', index + 1);
		if (index == string::npos){
			break;
		}
		string token(_line, start, index - start);
		GameSet gameSet(token);
		_sets.emplace_back(gameSet);
	}
	string token(_line, start, _line.size() - start);
	GameSet gameSet(token);
	_sets.emplace_back(gameSet);
}

auto Game::isValid() -> bool
{
	bool valid = true;
	for (auto& gameSet : _sets) {
		if (!gameSet.isValid()){
			valid = false;
			break;
		}
	}
	return valid;
}

auto Game::fewestBlues() -> int
{
	int count = 0;
	for (auto& gameSet : _sets) {
		int newCount = gameSet.countBlue();
		if (newCount > count) {
			count = newCount;
		}
	}
	return count;
}

auto Game::fewestReds() -> int
{
	int count = 0;
	for (auto& gameSet : _sets) {
		int newCount = gameSet.countRed();
		if (newCount > count) {
			count = newCount;
		}
	}
	return count;
}

auto Game::fewestGreens() -> int
{
	int count = 0;
	for (auto& gameSet : _sets) {
		int newCount = gameSet.countGreen();
		if (newCount > count) {
			count = newCount;
		}
	}
	return count;
}
