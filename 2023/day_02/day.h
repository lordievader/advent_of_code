#pragma once
#include <iostream>
#include <ostream>
#include <regex>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Day
{
public:
	Day(unordered_map<string, string> flags, vector<string> contents);
	Day(Day&) = default;
	Day(Day&&) = default;
	auto operator=(Day&& other) -> Day& = default;
	auto operator=(Day const& other) -> Day& = default;
	virtual ~Day() = default;

	auto solvePartOne() -> void;
	auto solvePartTwo() -> void;

private:
	unordered_map<string, string> _flags;
	vector<string> _contents;
};

class GameSet
{
public:
	GameSet(string line);
	GameSet(GameSet&) = default;
	GameSet(GameSet&&) = default;
	auto operator=(GameSet&& other) -> GameSet& = default;
	auto operator=(GameSet const& other) -> GameSet& = default;
	virtual ~GameSet() = default;

	friend auto operator<<(ostream& stream, GameSet& game) -> ostream&;

	auto getLine() -> string {return _line;};
	auto countBlue() -> int;
	auto countRed() -> int;
	auto countGreen() -> int;
	auto isValid() -> bool;

private:
	string _line;
	regex _blueRegex = regex("(\\d+) blue");
	regex _greenRegex = regex("(\\d+) green");
	regex _redRegex = regex("(\\d+) red");
};

class Game
{
public:
	Game(string line);
	Game(Game&) = default;
	Game(Game&&) = default;
	auto operator=(Game&& other) -> Game& = default;
	auto operator=(Game const& other) -> Game& = default;
	virtual ~Game() = default;

	friend auto operator<<(ostream& stream, Game& game) -> ostream&;

	auto getLine() -> string { return _line; };
	auto getId() -> int { return _id; };
	auto isValid() -> bool;

	auto fewestBlues() -> int;
	auto fewestReds() -> int;
	auto fewestGreens() -> int;

private:
	int _id = 0;
	string _line;
	vector<GameSet> _sets;
	regex _idRegex = regex("Game (\\d+):");

	auto parseLine() -> void;
	auto parseSets() -> void;
	auto numberOfSets() -> size_t { return _sets.size(); };
};

