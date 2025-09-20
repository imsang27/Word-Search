"""
언어 설정 및 단어 리스트를 관리하는 모듈
"""

# 언어별 설정
LANGUAGE_CONFIGS = {
    "영어": {
        "words": ["APPLE", "BANANA", "ORANGE", "GRAPE", "STRAWBERRY", "WATERMELON", "PINEAPPLE", "MANGO"],
        "size": 15,
        "random_chars": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    },
    "한글": {
        "words": ["사과", "바나나", "오렌지", "포도", "딸기", "수박", "키위", "체리", "파인애플", "망고"],
        "size": 20,
        "random_chars": "가나다라마바사아자차카타파하거너더러머버서어저처커터퍼허고노도로모보소오조초코토포호구누두루무부수우주추쿠투푸후"
    }
}

def get_language_config(language):
    """선택된 언어의 설정을 반환합니다."""
    return LANGUAGE_CONFIGS.get(language, LANGUAGE_CONFIGS["한글"])

def get_available_languages():
    """사용 가능한 언어 목록을 반환합니다."""
    return list(LANGUAGE_CONFIGS.keys())
