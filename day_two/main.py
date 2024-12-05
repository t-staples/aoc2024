from time import perf_counter
class Solution:
    def __init__(self):
        self._reports = []

    def parse_input(self):
        with open('puzzle_input.txt') as f:
            _lines = f.readlines()
        
        for line in _lines:
            _data = [int (x) for x in line.strip('\n').split()]
            self._reports.append(_data)

    def helper(self, report) -> None:
        _is_safe = True
        _is_incrementing = (report[1] - report[0]) > 0
        for x in range(len(report) - 1):
            _difference = report[x + 1] - report[x] 
            if abs(_difference) < 1 or abs(_difference) > 3:
                _is_safe = False
                break
            else:
                if _is_incrementing:
                    if _difference < 0:
                        _is_safe = False
                        break
                else:
                    if _difference > 0:
                        _is_safe = False
                        break
        return _is_safe
    
    def part_two(self):
        _safe_reports_counter = 0
        for report in self._reports:
            if self.helper(report):
                _safe_reports_counter += 1
            else:
                for x in range(len(report)):
                    _copy = report.copy()
                    _copy.pop(x)
                    if self.helper(_copy):
                        _safe_reports_counter += 1
                        break
        print(_safe_reports_counter)

    def part_one(self):
        _safe_reports_counter = 0
        for report in self._reports:
            if self.helper(report):
                _safe_reports_counter += 1
        print(_safe_reports_counter)


if __name__ == "__main__":
    _solution = Solution()
    _solution.parse_input()
    _solution.part_one()
    _solution.part_two()
    
