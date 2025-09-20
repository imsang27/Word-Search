import random

# 언어 선택
def select_language():
    print("언어를 선택하세요:")
    print("1. 영어 (ㅇ)")
    print("2. 한글 (ㅎ)")
    while True:
        choice = input("선택 (1, 2, ㅇ, 또는 ㅎ): ").strip()
        if choice in ["1", "ㅇ", "영어"]:
            return "영어"
        elif choice in ["2", "ㅎ", "한글"]:
            return "한글"
        else:
            print("잘못된 선택입니다. 1, 2, ㅇ, 또는 ㅎ를 입력하세요.")

LANGUAGE = select_language()

# 퍼즐 기본 세팅
if LANGUAGE == "영어":
    words = ["APPLE", "BANANA", "ORANGE", "GRAPE", "STRAWBERRY", "WATERMELON"]
    size = 15
    random_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
elif LANGUAGE == "한글":
    words = ["사과", "바나나", "오렌지", "포도", "딸기", "수박", "키위", "체리"]
    size = 20  # 한글은 2바이트이므로 더 큰 그리드 필요
    random_chars = "가나다라마바사아자차카타파하거너더러머버서어저처커터퍼허고노도로모보소오조초코토포호구누두루무부수우주추쿠투푸후"

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
placed_words = []
failed_words = []

for word in words:
    if place_word(word):
        placed_words.append(word)
    else:
        failed_words.append(word)

if failed_words:
    print(f"다음 단어들을 배치할 수 없습니다: {', '.join(failed_words)}")
    print(f"성공적으로 배치된 단어: {', '.join(placed_words)}")
    words = placed_words  # 배치된 단어들만 사용

# 빈칸 랜덤 채우기
for y in range(size):
    for x in range(size):
        if grid[y][x] == " ":
            grid[y][x] = random.choice(random_chars)

# 출력
print(f"\n=== {LANGUAGE} 단어 찾기 퍼즐 ===")
print(f"찾을 단어들: {', '.join(words)}")
print(f"그리드 크기: {size}x{size}")
print("\n퍼즐:")
print("=" * (size * 3))

for row in grid:
    if LANGUAGE == "한글":
        # 한글은 2바이트이므로 공백을 적절히 조정
        print(" ".join(f"{cell:^2}" for cell in row))
    else:
        print(" ".join(row))

print("=" * (size * 3))
print(f"\n찾을 단어: {', '.join(words)}")

# 다시 생성할지 묻기
while True:
    again = input("\n다른 퍼즐을 생성하시겠습니까? (y/n): ").strip().lower()
    if again in ['y', 'yes', '예', 'ㅇ']:
        print("\n새로운 퍼즐을 생성합니다...")
        # 프로그램을 다시 시작하려면 이 부분을 수정하거나 재실행하세요
        break
    elif again in ['n', 'no', '아니오', 'ㄴ']:
        print("게임을 종료합니다.")
        break
    else:
        print("y 또는 n을 입력하세요.")
