#include "day01.h"
#include "../lib/functions.h"
#include <stdexcept>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

Day01::Day01(unordered_map<string, string> flags, vector<string> contents)
: _flags(std::move(flags))
, _contents(std::move(contents))
{
}


auto Day01::solvePartOne() -> void
{
	vector<Line> lines;
	for (auto const& line: _contents) {
		Line lineObj(line);
		lines.emplace_back(lineObj);
	}

	uint64_t answer = 0;
	for (auto& line : lines) {
		answer += line.getDigits();
	}
	cout << "Answer part 1: " << answer << endl;
}

auto Day01::solvePartTwo() -> void
{
	vector<Line> lines;
	for (auto const& line: _contents) {
		Line lineObj(line, true);
		lines.emplace_back(lineObj);
	}

	uint64_t answer = 0;
	for (auto& line : lines) {
		answer += line.getDigits();
	}
	cout << "Answer part 2: " << answer << endl;
}

Line::Line(string line, bool writtenOutDigits)
: _line(std::move(line))
, _digits(0)
{
	this->parseLine(writtenOutDigits);
}

auto Line::parseLine(bool writtenOutDigits) -> void {
	auto first = _line.begin();
	auto last = _line.end();
	match_results<decltype(first)> match;

	vector<string> digits;
	while ( regex_search(first, last, match, _digitsRegex) ) {
		string matchStr = match.str();
		if (writtenOutDigits) {
			if (_digitMap.contains(matchStr)) {
				digits.emplace_back(to_string(_digitMap[matchStr]));
			} else {
				digits.emplace_back(match.str());
			}
		} else if (!writtenOutDigits && !_digitMap.contains(matchStr)){
			digits.emplace_back(match.str());
		}
		first = std::next(match.prefix().second);
	}
	if (digits.empty()) {
		return;
	}
	string firstAndLastString = digits.front() + digits.back();
	_digits = stoi(firstAndLastString);
}

auto operator<<(ostream& stream, Line& line) -> ostream&
{
	stream << line.getLine() << " -> " << line.getDigits() << endl;
	return stream;
}
