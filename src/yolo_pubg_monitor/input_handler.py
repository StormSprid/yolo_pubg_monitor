import keyboard


def on_tab_pressed():
    print(f'TAB has been pressed')

def start_listening(on_tab_callback):
    """Запускает прослушивание клавиш."""
    print(f'script has been started')

    keyboard.add_hotkey("tab",on_tab_callback)

    keyboard.wait('esc')
    print('script stopped')

if __name__ == "__main__":
    start_listening()