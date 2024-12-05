from time import perf_counter
class Solution:
    def __init__(self):
        self._rules = []
        self._page_numbers = []
        self._digits_to_rules_dictionary = {}

    def parse_input(self):
        with open('puzzle_input.txt') as f:
            _lines = f.readlines()

        end_of_rules_hit = False
        for line in _lines:
            if line == "\n":
                end_of_rules_hit = True
            elif not end_of_rules_hit:
                self._rules.append(line.rstrip('\n'))
            elif end_of_rules_hit:
                self._page_numbers.append(line.rstrip('\n').split(','))
        
    def part_one(self):
        for rule in self._rules:
            nums = rule.split('|')
            num1 = int(nums[0])
            num2 = int(nums[1])
            if num1 in self._digits_to_rules_dictionary:
                self._digits_to_rules_dictionary[num1].add(num2)
            else:
                self._digits_to_rules_dictionary[num1] = {num2}
        
        _sum = 0
        for page_line in self._page_numbers:
            if (self.check_line_valid(page_line)):
                _mid_index = int(len(page_line) / 2)
                _sum += int(page_line[_mid_index])
        return _sum

    def part_two(self):
        _incorrectly_ordered = []

        for page_line in self._page_numbers:
            if (not self.check_line_valid(page_line)):
                _incorrectly_ordered.append(page_line)
        _sum = 0
        for incorrect_page in _incorrectly_ordered:
            for x in range(len(incorrect_page)):
                for y in range(x + 1, len(incorrect_page)):
                    if int(incorrect_page[x]) in self._digits_to_rules_dictionary:
                        if int(incorrect_page[y]) not in self._digits_to_rules_dictionary[int(incorrect_page[x])]:
                            buffer = incorrect_page[x]
                            incorrect_page[x] = incorrect_page[y]
                            incorrect_page[y] = buffer
                    else:
                        if int(incorrect_page[y]) in self._digits_to_rules_dictionary:
                            if int(incorrect_page[x]) in self._digits_to_rules_dictionary[int(incorrect_page[y])]:
                                buffer = incorrect_page[x]
                                incorrect_page[x] = incorrect_page[y]
                                incorrect_page[y] = buffer

            _mid_index = int(len(incorrect_page) / 2)
            _sum += int(incorrect_page[_mid_index])
        return _sum


    def check_line_valid(self, line):
        for x in range(len(line)):
            for y in range(x+1,len(line)):
                if int(line[x]) in self._digits_to_rules_dictionary:
                    if int(line[y]) not in self._digits_to_rules_dictionary[int(line[x])]:
                        return False
                else:
                    return False
        return True

if __name__ == "__main__":
    _solution = Solution()
    _solution.parse_input()
    _start = perf_counter()
    _part_one = _solution.part_one()
    _part_two = _solution.part_two()
    _end = perf_counter()
    print(f"Duration {_end - _start} Part One Sol: {_part_one} Part Two Sol: {_part_two}")