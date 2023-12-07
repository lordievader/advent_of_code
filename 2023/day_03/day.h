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


class Grid
{
public:
	Grid(vector<string> lines);
	Grid(Grid&) = default;
	Grid(Grid&&) = default;
	auto operator=(Grid&& other) -> Grid& = default;
	auto operator=(Grid const& other) -> Grid& = default;
	virtual ~Grid() = default;

	friend auto operator<<(ostream& stream, Grid& grid) -> ostream&;

	auto getLines() -> vector<string> { return _lines; };
	auto getGrid() -> vector<vector<char>> { return _grid; };
	auto getSymbolLocations() -> vector<pair<int, int>> { return _symbols; };
	auto adjecentNumbers(int row, int colum) -> vector<int>;

	auto getGearLocations() -> vector<pair<int, int>>;

private:
	vector<string> _lines;
	vector<vector<char>> _grid;
	vector<pair<int, int>> _symbols;

	auto parseGrid() -> void;
	auto findSymbols() -> void;
	auto findFullNumber(size_t row, size_t colum) -> int;
};
