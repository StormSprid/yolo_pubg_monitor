from yolo_pubg_monitor.audio_feedback import play_screenshot_sound
from yolo_pubg_monitor.vision import take_screenshot
from yolo_pubg_monitor.input_handler import start_listening


def start_pipeline():
    """Основной шаг пайплайна при нажатии клавиши."""
    path = take_screenshot()
    play_screenshot_sound()
    print(f'Screenshot has been taken {path}')
    # В будущем здесь добавится:
    # 1. Вызов YOLO (модуль детекции)
    # 2. Вызов RAG (модуль логики)
    # 3. Вызов TTS (модуль голоса

def main():
    start_listening(on_tab_callback=start_pipeline)

if __name__ == "__main__":
    main()