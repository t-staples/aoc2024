import re
from time import perf_counter

class Solution:
    def __init__(self):
        self._input_string = ""
        self._regex_pattern = r"mul\((\d+,\d+)\)"
        self._do_pattern = r"do\(\)"
        self._dont_pattern = r"don't\(\)"


    def parse_input(self):
        with open('puzzle_input.txt') as f:
            lines = f.readlines()

        self._input_string = "".join(lines)

    def part_one(self):
        matches = re.findall(self._regex_pattern, self._input_string)
        _result = 0
        for match in matches:
            integers = match.split(',')
            _result += int(integers[0]) * int(integers[1]) 
        print(_result)

    def part_two(self):
        _enabled:bool = True
        _final_string = ""
        _do_locations = set()
        _dont_locations = set()
        _test = re.finditer(self._do_pattern, self._input_string)
        _test2 = re.finditer(self._dont_pattern, self._input_string)
        for test in _test:
            _do_locations.add(test.start())
        for test2 in _test2:
            _dont_locations.add(test2.start())

        for count, character in enumerate(self._input_string):
            if _enabled:
                _final_string += character
            
            # Check if our index is equal to don't start 
            if (count in _dont_locations):
                _enabled = False
            # Check if our index is equal to a start 
            if count in _do_locations:
                _enabled = True
        
        matches = re.findall(self._regex_pattern, _final_string)
        _result = 0
        for match in matches:
            integers = match.split(',')
            _result += int(integers[0]) * int(integers[1]) 
        print(_result)

if __name__ == "__main__":
    _solution = Solution()
    _solution_start = perf_counter()
    _solution.parse_input()
    _solution.part_one()
    _solution.part_two()
    _solution_end = perf_counter()
    print(f"Duration {_solution_end - _solution_start}")
