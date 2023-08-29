def solution(park, routes):
    answer = []
    is_continue = True
    # find 현재위치
    for row, line in enumerate(park):
        if not is_continue:
            break
        for col, cell in enumerate(line):
            if cell == 'S':
                answer = [row, col]
                is_continue = False
                break
    
    for route in routes:
        cur_row = answer[0]
        cur_col = answer[1]
        route_direction, route_distance = route.split()
        route_distance = int(route_distance)
        is_okay = True

        if route_direction == 'E':
            if cur_col + route_distance >= len(park[0]):
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row][cur_col + i] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row, cur_col + route_distance]

        elif route_direction == 'W':
            if cur_col - route_distance < 0:
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row][cur_col - i] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row, cur_col - route_distance]

        elif route_direction == 'S':
            if cur_row + route_distance >= len(park[0]):
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row + i][cur_col] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row + route_distance, cur_col]

        else:
            if cur_row - route_distance < 0:
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row - i][cur_col] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row - route_distance, cur_col]

    return answer


"""
변수명을 명확하게 쓰려다 더 보기 번잡해진듯
동서남북이면, 각 방향별로 증감값을 정해놓으면 중복되는 코드 양 줄 것
클래스 사용도 고려해볼 것


다른 답안:
class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]

"""