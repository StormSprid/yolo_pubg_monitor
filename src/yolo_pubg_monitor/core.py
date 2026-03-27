from vision import take_screenshot
from input_handler import start_listening


def start_pipeline():
    """Основной шаг пайплайна при нажатии клавиши."""
    path = take_screenshot()
    print(f'Screenshot has been taken {path}')
    # В будущем здесь добавится:
    # 1. Вызов YOLO (модуль детекции)
    # 2. Вызов RAG (модуль логики)
    # 3. Вызов TTS (модуль голоса

if __name__ == "__main__":
    start_listening(on_tab_callback=start_pipeline)