import random

# 퍼즐 기본 세팅
words = ["APPLE", "BANANA", "ORANGE", "GRAPE"]
size = 12
grid = [[" " for _ in range(size)] for _ in range(size)]

# 방향 (dx, dy)
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def can_place(word, x, y, dx, dy):
    for i, ch in enumerate(word):
        nx, ny = x + dx*i, y + dy*i
        if not (0 <= nx < size and 0 <= ny < size):
            return False
        if grid[ny][nx] not in (" ", ch):
            return False
    return True

def place_word(word):
    random.shuffle(directions)
    for _ in range(100):
        x, y = random.randrange(size), random.randrange(size)
        for dx, dy in directions:
            if can_place(word, x, y, dx, dy):
                for i, ch in enumerate(word):
                    grid[y + dy*i][x + dx*i] = ch
                return True
    return False

# 단어 넣기
for word in words:
    place_word(word)

# 빈칸 랜덤 채우기
for y in range(size):
    for x in range(size):
        if grid[y][x] == " ":
            grid[y][x] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# 출력
for row in grid:
    print(" ".join(row))
