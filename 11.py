from copy import deepcopy

class Chair:
    def __init__(self, x, y, occupied=False):
        self.x = x
        self.y = y
        self.occupied = occupied

    def __str__(self):
        return f"Chair: ({self.x},{self.y})"

class ChairMap:
    def __init__(self, raw, occupancy_limit=4):
        self.raw = raw
        self.chairs = {}
        self.map = self._parse_raw_input()
        self.has_changed = True
        self.occupancy_limit = occupancy_limit

    def __str__(self):
        blob = ""
        for y in range(self.y_max):
            row = ""
            for x in range(self.x_max):
                key = (x,y)
                if key in self.chairs:
                    if self.chairs[key].occupied:
                        row += "#"
                    else:
                        row += "L"
                else:
                    row += "."
            blob += row + "\n"
        return blob 

    def _parse_raw_input(self):
        for y, line in enumerate(self.raw.strip().split("\n")):
            for x, char in enumerate(line):
                if char == "L":
                    self.chairs[(x,y)] = Chair(x,y)
        self.x_max = x + 1
        self.y_max = y + 1

    def get_chair(self, x, y):
        return self.chairs.get((x,y), None)

    def cycle_seats_adjacent(self):
        new_chairs = deepcopy(self.chairs)
        has_changed = False
        for chair in new_chairs.values():
            occupation_count = 0
            for x in range(chair.x - 1, chair.x + 2):
                for y in range(chair.y - 1, chair.y +2):
                    if x == chair.x and y == chair.y:
                            continue
                    if chair_map.get_chair(x,y) and chair_map.get_chair(x,y).occupied:
                        occupation_count += 1
            if not chair.occupied and occupation_count == 0:
                chair.occupied = True
                has_changed = True
            if chair.occupied and occupation_count >= self.occupancy_limit:
                chair.occupied = False
                has_changed = True
        self.chairs = new_chairs
        self.has_changed = has_changed

    def cycle_seats_seen(self):
        new_chairs = deepcopy(self.chairs)
        has_changed = False
        for chair in new_chairs.values():
            occupation_count = 0
            for x in range(chair.x - 1, chair.x + 2):
                for y in range(chair.y - 1, chair.y +2):
                    if x == chair.x and y == chair.y:
                            continue
                    if chair_map.get_chair(x,y):
                        if chair_map.get_chair(x,y).occupied:
                            occupation_count += 1
                    else:
                        x_delta = x - chair.x
                        y_delta = y - chair.y
                        # if anyone actually reads this I hate it and I'm sorry
                        if x_delta > 0 and y_delta > 0:
                            # Bottom Right - x and y march up to x-/y-max
                            i = x + 1
                            j = y + 1
                            while i < self.x_max and j < self.y_max:
                                if chair_map.get_chair(i,j):
                                    if chair_map.get_chair(i,j).occupied:
                                        occupation_count += 1
                                    break
                                i += 1
                                j += 1
                        elif x_delta > 0 and y_delta < 0:
                            # Top Right - x marches to x_max and y marches to 0
                            i = x + 1
                            j = y - 1
                            while i < self.x_max and j >= 0:
                                if chair_map.get_chair(i,j):
                                    if chair_map.get_chair(i,j).occupied:
                                        occupation_count += 1
                                    break
                                i += 1
                                j -= 1
                        elif x_delta > 0 and y_delta == 0:
                            # Right - x marches to x_max
                            for i in range(x, self.x_max):
                                if chair_map.get_chair(i,y):
                                    if chair_map.get_chair(i,y).occupied:
                                        occupation_count += 1
                                    break
                        elif x_delta == 0 and y_delta > 0:
                            # Down - y marches to y_max
                            for j in range(y, self.y_max):
                                if chair_map.get_chair(x,j):
                                    if chair_map.get_chair(x,j).occupied:
                                        occupation_count += 1
                                    break
                        elif x_delta == 0 and y_delta < 0:
                            # Up - y marches to 0
                            for j in range(y, -1, -1):
                                if chair_map.get_chair(x,j):
                                    if chair_map.get_chair(x,j).occupied:
                                        occupation_count += 1
                                    break
                        elif x_delta < 0 and y_delta < 0:
                            # Top Left - x and y march to 0
                            i = x - 1
                            j = y - 1
                            while i >= 0 and j >= 0:
                                if chair_map.get_chair(i,j):
                                    if chair_map.get_chair(i,j).occupied:
                                        occupation_count += 1
                                    break
                                i -= 1
                                j -= 1
                        elif x_delta < 0 and y_delta == 0:
                            # Left - x marches to 0
                            for i in range(x, -1, -1):
                                if chair_map.get_chair(i,y):
                                    if chair_map.get_chair(i,y).occupied:
                                        occupation_count += 1
                                    break
                        elif x_delta < 0 and y_delta > 0:
                            # Bottom Left - x marches to 0 and y marches to y_max
                            i = x - 1
                            j = y + 1
                            while i >= 0 and j < self.y_max:
                                if chair_map.get_chair(i,j):
                                    if chair_map.get_chair(i,j).occupied:
                                        occupation_count += 1
                                    break
                                i -= 1
                                j += 1

            if not chair.occupied and occupation_count == 0:
                chair.occupied = True
                has_changed = True
            if chair.occupied and occupation_count >= self.occupancy_limit:
                chair.occupied = False
                has_changed = True
        self.chairs = new_chairs
        self.has_changed = has_changed

    def occupied_seats(self):
        tot = 0
        for chair in self.chairs.values():
            if chair.occupied:
                tot += 1
        return tot

if __name__ == "__main__":
    with open("input11.txt","r") as f:
        chair_map = ChairMap(f.read(), 5)

    print(f"Cycling seats and allowing {chair_map.occupancy_limit} neighbors.\n")
    # print(f"Initial seat state:\n{chair_map}")
    cycles = 0

    while chair_map.has_changed:
        chair_map.cycle_seats_seen()
        cycles += 1
        if cycles % 10 == 0:
            print(f"Still cycling seats.\n\tOccupied Count: {chair_map.occupied_seats()}\n\tCycles Performed: {cycles}\n")
            # print(f"Current state:\n{chair_map}")

    print(f"Cycling complete. There are {chair_map.occupied_seats()} occupied seats.")
