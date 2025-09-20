"""
단어 찾기 퍼즐 생성 및 관리 클래스
"""
import random
from .language_config import get_language_config

class WordSearchPuzzle:
    def __init__(self, language="한글"):
        self.language = language
        self.config = get_language_config(language)
        self.words = self.config["words"].copy()
        self.size = self.config["size"]
        self.random_chars = self.config["random_chars"]
        self.grid = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        self.placed_words = []
        self.failed_words = []
    
    def can_place(self, word, x, y, dx, dy):
        """단어를 해당 위치에 배치할 수 있는지 확인합니다."""
        for i, ch in enumerate(word):
            nx, ny = x + dx*i, y + dy*i
            if not (0 <= nx < self.size and 0 <= ny < self.size):
                return False
            if self.grid[ny][nx] not in (" ", ch):
                return False
        return True
    
    def place_word(self, word):
        """단어를 그리드에 배치합니다."""
        random.shuffle(self.directions)
        for _ in range(100):  # 최대 100번 시도
            x, y = random.randrange(self.size), random.randrange(self.size)
            for dx, dy in self.directions:
                if self.can_place(word, x, y, dx, dy):
                    for i, ch in enumerate(word):
                        self.grid[y + dy*i][x + dx*i] = ch
                    return True
        return False
    
    def generate_puzzle(self):
        """퍼즐을 생성합니다."""
        # 단어 배치
        for word in self.words:
            if self.place_word(word):
                self.placed_words.append(word)
            else:
                self.failed_words.append(word)
        
        # 실패한 단어가 있으면 알림
        if self.failed_words:
            print(f"다음 단어들을 배치할 수 없습니다: {', '.join(self.failed_words)}")
            print(f"성공적으로 배치된 단어: {', '.join(self.placed_words)}")
            self.words = self.placed_words  # 배치된 단어들만 사용
        
        # 빈칸 랜덤 채우기
        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] == " ":
                    self.grid[y][x] = random.choice(self.random_chars)
    
    def reset_puzzle(self):
        """퍼즐을 초기화합니다."""
        self.grid = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.placed_words = []
        self.failed_words = []
        self.words = self.config["words"].copy()
    
    def get_grid(self):
        """현재 그리드를 반환합니다."""
        return self.grid
    
    def get_words(self):
        """찾을 단어 목록을 반환합니다."""
        return self.words
    
    def get_placed_words(self):
        """성공적으로 배치된 단어 목록을 반환합니다."""
        return self.placed_words
