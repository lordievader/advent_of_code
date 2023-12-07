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

auto Day::solvePartOne() -> void {
	Grid grid(_contents);

	int answer = 0;
	for (const auto& location: grid.getSymbolLocations()) {
		vector<int> adjecentNumbers = grid.adjecentNumbers(location.first, location.second);
		for (const auto& number: adjecentNumbers) {
			answer += number;
		}
	}
	cout << "Answer to part one: " << answer << endl;
}

auto Day::solvePartTwo() -> void {
	Grid grid(_contents);

	int answer = 0;
	for (const auto& location: grid.getGearLocations()) {
		vector<int> adjecentNumbers = grid.adjecentNumbers(location.first, location.second);
		if (adjecentNumbers.size() != 2) {
			continue;
		}
		int gearRatio = adjecentNumbers[0] * adjecentNumbers[1];
		answer += gearRatio;
	}
	cout << "Answer to part one: " << answer << endl;
}

Grid::Grid(vector<string> lines)
: _lines(std::move(lines))
{
	this->parseGrid();
}

auto operator<<(ostream& stream, Grid& grid) -> ostream&
{
	vector<vector<char>> gridGrid = grid.getGrid();
	stream << "Lines in grid: " << gridGrid.size() << endl;
	for (const auto& line : gridGrid) {
		for (const auto& character: line) {
			stream << character;
		}
		stream << endl;
	}
	return stream;
}

auto Grid::parseGrid() -> void
{
	vector<vector<char>> grid;
	for (const auto& line: _lines) {
		vector<char> parsedLine;
		for (auto character : line) {
			parsedLine.emplace_back(character);
		}
		grid.emplace_back(parsedLine);
	}
	_grid = grid;
	this->findSymbols();
}

auto Grid::findSymbols() -> void
{
	_symbols.clear();
	const vector<char> nonSymbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'};
	int rowIndex = 0;
	for (const auto& row: _grid) {
		int columnIndex = 0;
		for (const auto& column: row) {
			auto iterator = find(nonSymbols.begin(), nonSymbols.end(), column);
			if (iterator == nonSymbols.end()) {
				// This is a symbol
				_symbols.emplace_back(rowIndex, columnIndex);
				vector<int> numbers = this->adjecentNumbers(rowIndex, columnIndex);
			}
			columnIndex += 1;
		}
		rowIndex += 1;
	}
}

auto Grid::adjecentNumbers(int row, int column) -> vector<int>
{
	const vector<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	vector<int> adjecentNumbers;

	// Check all spots around symbol for digits
	size_t startRow = row - 1 < 0 ? 0 : row - 1;
	size_t endRow = row + 2 > _grid.size() ? _grid.size() : row + 2;
	size_t startColumn = column - 1 < 0 ? 0 : column - 1;
	size_t endColumn = column + 2 > _grid[0].size() ? _grid[0].size() : column + 2;
	for (size_t rowIndex = startRow; rowIndex < endRow; rowIndex++) {
		for (size_t columnIndex = startColumn; columnIndex < endColumn; columnIndex++) {
			char value = _grid[rowIndex][columnIndex];
			auto iterator = find(digits.begin(), digits.end(), value);
			if (iterator != digits.end()) {
				// This is a digit
				int adjecentNumber = this->findFullNumber(rowIndex, columnIndex);
				auto iterator = find(adjecentNumbers.begin(), adjecentNumbers.end(), adjecentNumber);
				if (iterator == adjecentNumbers.end()) {
					adjecentNumbers.emplace_back(adjecentNumber);
				}
			}
		}
	}
	return adjecentNumbers;
}

auto Grid::findFullNumber(size_t row, size_t column) -> int
{
	const vector<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	size_t start = column;
	bool digitFound = true;
	while (digitFound) {
		size_t columnIndex = start - 1;
		char value = _grid[row][columnIndex];
		auto iterator = find(digits.begin(), digits.end(), value);
		if (iterator != digits.end()) {
			// This is a digit
			start = columnIndex;
		} else {
			digitFound = false;
		}
	}

	size_t end = column;
	digitFound = true;
	while (digitFound) {
		size_t columnIndex = end + 1;
		char value = _grid[row][columnIndex];
		auto iterator = find(digits.begin(), digits.end(), value);
		if (iterator != digits.end()) {
			// This is a digit
			end = columnIndex;
		} else {
			digitFound = false;
		}
	}
	string fullNumber;
	for (size_t index = start; index <= end; index++) {
		fullNumber += _grid[row][index];
	}
	return stoi(fullNumber);
}

auto Grid::getGearLocations() -> vector<pair<int,int>>
{
	vector<pair<int, int>> gears;
	for(const auto& symbol: this->getSymbolLocations()){
		char value = _grid[symbol.first][symbol.second];
		if (value == '*') {
			gears.emplace_back(symbol);
		}
	}
	return gears;
}
