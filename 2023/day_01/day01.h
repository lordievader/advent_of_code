#pragma once
#include <iostream>
#include <ostream>
#include <regex>
#include <unordered_map>
#include <vector>

using namespace std;

class Day01
{
public:
	Day01(unordered_map<string, string> flags, vector<string> contents);
	Day01(Day01&) = default;
	Day01(Day01&&) = default;
	auto operator=(Day01&& other) -> Day01& = default;
	auto operator=(Day01 const& other) -> Day01& = default;
	virtual ~Day01() = default;
	auto solvePartOne() -> void;
	auto solvePartTwo() -> void;

private:
	unordered_map<string, string> _flags;
	vector<string> _contents;
};

class Line
{
public:
	Line(string line, bool writtenOutDigits = false);
	Line(Line&) = default;
	Line(Line&&) = default;
	auto operator=(Line&& other) -> Line& = default;
	auto operator=(Line const& other) -> Line& = default;
	virtual ~Line() = default;

	friend auto operator<<(ostream& stream, Line& line) -> ostream&;

	auto getLine() -> string { return _line; };
	auto getDigits() -> int { return _digits; };

private:
	string _line;
	regex _digitsRegex = regex("(\\d|one|two|three|four|five|six|seven|eight|nine)");
	int _digits;

	std::map<string, int> _digitMap{
		{"one", 1},
		{"two", 2},
		{"three", 3},
		{"four", 4},
		{"five", 5},
		{"six", 6},
		{"seven", 7},
		{"eight", 8},
		{"nine", 9},
	};

	auto parseLine(bool writtenOutDigits = false) -> void;
};
