from time import perf_counter

class Solution:
    def __init__(self):
        self._list_one = []
        self._list_two = []

    
    def read_puzzle_input(self):
        with open('puzzle_input.txt') as f:
            input = f.readlines()
        
        for entry in input:
            _entries = entry.split("   ")
            self._list_one.append(int(_entries[0]))
            self._list_two.append(int(_entries[1].split("\n")[0]))

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
        # Create hash map of second list 
        # Containing num : frequency 
        _part_two_start = perf_counter()
        _scaling_hashmap = {}
        _similarity_score = 0
        for num in self._list_two:
            if num not in _scaling_hashmap:
                _scaling_hashmap[num] = 1
            else:
                _scaling_hashmap[num] += 1
        # Calculate Scaling score
        for num in self._list_one:
            if num in _scaling_hashmap:
                _similarity_score += num * _scaling_hashmap[num]
        _part_two_end = perf_counter()
        print(f"Part Two Answer {_similarity_score} Duration {_part_two_end - _part_two_start}")




if __name__ == "__main__":
    _solution = Solution()
    _solution.read_puzzle_input()
    _solution.part_one()
    _solution.part_two()
