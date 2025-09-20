"""
단어 찾기 퍼즐 게임 패키지
"""

__version__ = "1.0.0"
__author__ = "Word Search Game Team"

from .word_search_game import WordSearchGame
from .word_search_puzzle import WordSearchPuzzle
from .ui_interface import UIInterface
from .language_config import get_language_config, get_available_languages

__all__ = [
    "WordSearchGame",
    "WordSearchPuzzle", 
    "UIInterface",
    "get_language_config",
    "get_available_languages"
]
