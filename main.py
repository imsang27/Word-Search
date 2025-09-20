"""
단어 찾기 퍼즐 게임 메인 실행 파일
"""
from src.word_search_game import WordSearchGame

def main():
    """메인 함수"""
    game = WordSearchGame()
    game.run()

if __name__ == "__main__":
    main()
