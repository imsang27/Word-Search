"""
사용자 인터페이스 및 입력 처리를 담당하는 모듈
"""
from .language_config import get_available_languages

class UIInterface:
    def __init__(self):
        self.available_languages = get_available_languages()
    
    def select_language(self):
        """언어를 선택하도록 사용자에게 요청합니다."""
        print("언어를 선택하세요:")
        for i, lang in enumerate(self.available_languages, 1):
            if lang == "영어":
                print(f"{i}. {lang} (ㅇ)")
            elif lang == "한글":
                print(f"{i}. {lang} (ㅎ)")
            else:
                print(f"{i}. {lang}")
        
        while True:
            choice = input(f"선택 (1-{len(self.available_languages)}, ㅇ, 또는 ㅎ): ").strip()
            
            # 숫자로 선택
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(self.available_languages):
                    return self.available_languages[choice_num - 1]
            
            # 한글 자모로 선택
            elif choice in ["ㅇ", "영어"]:
                return "영어"
            elif choice in ["ㅎ", "한글"]:
                return "한글"
            
            # 언어명으로 직접 선택
            elif choice in self.available_languages:
                return choice
            
            else:
                print(f"잘못된 선택입니다. 1-{len(self.available_languages)}, ㅇ, 또는 ㅎ를 입력하세요.")
    
    def display_puzzle(self, puzzle):
        """퍼즐을 화면에 출력합니다."""
        print(f"\n=== {puzzle.language} 단어 찾기 퍼즐 ===")
        print(f"찾을 단어들: {', '.join(puzzle.get_words())}")
        print(f"그리드 크기: {puzzle.size}x{puzzle.size}")
        print("\n퍼즐:")
        print("=" * (puzzle.size * 3))
        
        grid = puzzle.get_grid()
        for row in grid:
            if puzzle.language == "한글":
                # 한글은 2바이트이므로 공백을 적절히 조정
                print(" ".join(f"{cell:^2}" for cell in row))
            else:
                print(" ".join(row))
        
        print("=" * (puzzle.size * 3))
        print(f"\n찾을 단어: {', '.join(puzzle.get_words())}")
    
    def ask_play_again(self):
        """다시 플레이할지 묻습니다."""
        while True:
            again = input("\n다른 퍼즐을 생성하시겠습니까? (y/n): ").strip().lower()
            if again in ['y', 'yes', '예', 'ㅇ']:
                return True
            elif again in ['n', 'no', '아니오', 'ㄴ']:
                return False
            else:
                print("y 또는 n을 입력하세요.")
    
    def display_welcome(self):
        """환영 메시지를 출력합니다."""
        print("=" * 50)
        print("🎯 단어 찾기 퍼즐 게임에 오신 것을 환영합니다! 🎯")
        print("=" * 50)
    
    def display_goodbye(self):
        """종료 메시지를 출력합니다."""
        print("\n게임을 종료합니다. 즐거운 시간이었습니다! 👋")
