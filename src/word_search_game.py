"""
단어 찾기 게임의 메인 로직을 관리하는 클래스
"""
from .word_search_puzzle import WordSearchPuzzle
from .ui_interface import UIInterface

class WordSearchGame:
    def __init__(self):
        self.ui = UIInterface()
        self.puzzle = None
    
    def start_game(self):
        """게임을 시작합니다."""
        self.ui.display_welcome()
        
        while True:
            # 언어 선택
            language = self.ui.select_language()
            
            # 퍼즐 생성
            self.puzzle = WordSearchPuzzle(language)
            self.puzzle.generate_puzzle()
            
            # 퍼즐 출력
            self.ui.display_puzzle(self.puzzle)
            
            # 다시 플레이할지 묻기
            if not self.ui.ask_play_again():
                break
        
        self.ui.display_goodbye()
    
    def run(self):
        """게임을 실행합니다."""
        try:
            self.start_game()
        except KeyboardInterrupt:
            print("\n\n게임이 중단되었습니다.")
            self.ui.display_goodbye()
        except Exception as e:
            print(f"\n오류가 발생했습니다: {e}")
            print("게임을 종료합니다.")
