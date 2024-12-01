from time import perf_counter

class Solution:
    def __init__(self):
        self._list_one = []
        self._list_two = []
        self._second_list_frequency_hash_map = {}
    
    def read_puzzle_input(self):
        with open('puzzle_input.txt') as f:
            input = f.readlines()
        
        for entry in input:
            _entries = entry.split("   ")
            _list_one_entry = int(_entries[0])
            _list_two_entry = int(_entries[1].split("\n")[0])
            self._list_one.append(_list_one_entry)
            self._list_two.append(_list_two_entry)
            if _list_two_entry not in self._second_list_frequency_hash_map:
                self._second_list_frequency_hash_map[_list_two_entry] = 1
            else:
                self._second_list_frequency_hash_map[_list_two_entry] += 1

    def part_one(self):
        _part_one_start = perf_counter()
        _total_distance_in_list = 0
        _sorted_list_one = sorted(self._list_one)
        _sorted_list_two = sorted(self._list_two)

        for x in range(len(_sorted_list_one)):
            _distance_apart = _sorted_list_two[x] - _sorted_list_one[x]
            _total_distance_in_list += abs(_distance_apart)
        _part_one_end = perf_counter()
        print(f"Part one Answer {_total_distance_in_list} Duration {_part_one_end - _part_one_start}")
        
    def part_two(self):
        _part_two_start = perf_counter()
        _similarity_score = 0
        for num in self._list_one:
            if num in self._second_list_frequency_hash_map:
                _similarity_score += num * self._second_list_frequency_hash_map[num]
        _part_two_end = perf_counter()
        print(f"Part Two Answer {_similarity_score} Duration {_part_two_end - _part_two_start}")

if __name__ == "__main__":
    _solution = Solution()
    _solution.read_puzzle_input()
    _solution.part_one()
    _solution.part_two()
