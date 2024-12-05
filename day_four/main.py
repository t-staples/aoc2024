from time import perf_counter
class Solution():
    def __init__(self):
        self._input_data = []

    def parse_input(self):
        with open('puzzle_input.txt') as f:
            _lines = f.readlines()
            for _line in _lines:
                self._input_data.append(_line.rstrip('\n').upper())


    def part_one(self):
        _max_rows = len(self._input_data)
        _max_cols = len(self._input_data[0])
        _xmas_counter = 0

        for row in range(len(self._input_data)):
            for col in range(len(self._input_data[0])):
                if (self._input_data[row][col] == 'X'):
                    if (row - 3 >= 0):
                        _north_string = "".join([   self._input_data[row][col],
                                                    self._input_data[row-1][col],
                                                    self._input_data[row-2][col],
                                                    self._input_data[row-3][col]])
                        if _north_string == "XMAS":
                            _xmas_counter += 1

                    if (row - 3 >= 0) and (col + 3 < _max_cols):
                        _north_east_string = "".join([self._input_data[row][col],
                                                      self._input_data[row-1][col+1],
                                                    self._input_data[row-2][col+2],
                                                    self._input_data[row-3][col+3]])
                        if _north_east_string == "XMAS":
                            _xmas_counter += 1

                    if (col + 3 < _max_cols):
                        _east_string = "".join([self._input_data[row][col],
                                                self._input_data[row][col+1],
                                                self._input_data[row][col+2],
                                                self._input_data[row][col+3]])
                        if _east_string == "XMAS":
                            _xmas_counter += 1

                    if (row + 3 < _max_rows) and (col + 3 < _max_cols):
                        _south_east_string = "".join([self._input_data[row][col],
                                                    self._input_data[row+1][col+1],
                                                    self._input_data[row+2][col+2],
                                                    self._input_data[row+3][col+3]])

                        if _south_east_string == "XMAS":
                            _xmas_counter += 1
                    
                    if (row + 3 < _max_rows):
                        _south_string = "".join([self._input_data[row][col],
                                                  self._input_data[row+1][col],
                                                self._input_data[row+2][col],
                                                self._input_data[row+3][col]])
                        if _south_string == "XMAS":
                            _xmas_counter += 1

                    
                    if (row + 3 < _max_rows) and (col - 3 >= 0):
                        south_west_string = "".join([self._input_data[row][col],
                                                    self._input_data[row+1][col - 1],
                                                    self._input_data[row+2][col - 2],
                                                    self._input_data[row+3][col - 3]])
                        if south_west_string == "XMAS":
                            _xmas_counter += 1

                    if (col -3 >= 0):
                        west_string = "".join([ self._input_data[row][col],
                                                self._input_data[row][col - 1],
                                                self._input_data[row][col - 2],
                                                self._input_data[row][col - 3]])
                        
                        if west_string == "XMAS":
                            _xmas_counter += 1

                    if (row -3 >= 0) and (col - 3 >= 0): 
                        north_west_string = "".join([self._input_data[row][col],
                                                    self._input_data[row-1][col - 1],
                                                    self._input_data[row-2][col - 2],
                                                    self._input_data[row-3][col - 3]])
                        if north_west_string == "XMAS":
                            _xmas_counter += 1

        return _xmas_counter
  
    def part_two(self):
        _max_rows = len(self._input_data)
        _max_cols = len(self._input_data[0])
        _xmas_counter = 0
        for row in range(len(self._input_data)):
            for col in range(len(self._input_data[0])):
                if (self._input_data[row][col] == 'A'):
                    
                    # Collect SW -> NE string 
                    sw_to_ne_string = ""
                    nw_to_se_string = ""
                    if (row + 1 < _max_rows) and (col - 1 >= 0) and (row -1 >= 0) and (col + 1 < _max_cols):
                        sw_to_ne_string = "".join([self._input_data[row+1][col-1],
                                                   self._input_data[row][col],
                                                   self._input_data[row-1][col+1]])
                    
                    # Collect NW -> SE String 
                    if (row - 1 >= 0) and (col -1 >= 0) and (row + 1 < _max_rows) and (col + 1 < _max_cols):
                        nw_to_se_string = "".join([self._input_data[row-1][col-1],
                                                   self._input_data[row][col],
                                                   self._input_data[row+1][col+1]])

                    # Collections of MAS and SAM 

                    if (sw_to_ne_string == "SAM" or sw_to_ne_string == "MAS") and (nw_to_se_string == "SAM" or nw_to_se_string == "MAS"):
                        _xmas_counter += 1
        return _xmas_counter

if __name__ == "__main__":
    _solution = Solution()
    _solution.parse_input()
    _start_time = perf_counter()
    part_one_answer = _solution.part_one()
    part_two_answer = _solution.part_two()
    _end_time = perf_counter()
    print(f"Part One {part_one_answer} Part Two {part_two_answer} Duration {_end_time - _start_time}")
