import part_1

class Frequency():
    def __init__(self):
        self.current_frequency = 0
        self.past_freqencies = []

    def new_frequency(self, frequency):
        self.past_freqencies.append(self.current_frequency)
        self.current_frequency += frequency

    def is_current_duplicate(self):
        return self.current_frequency in self.past_freqencies

def solution(numbers):
    int_numbers = part_1.to_int(numbers)
    length = len(int_numbers)
    frequency= Frequency()
    index = 0
    while frequency.is_current_duplicate() is False:
        number = int_numbers[index]
        frequency.new_frequency(number)
        index = (index + 1) % length

    return frequency.current_frequency
