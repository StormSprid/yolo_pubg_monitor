import mss
import os
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def take_screenshot(sub_dir="dataset/raw_screens"):
    """Делает скриншот и сохраняет его в указанную папку."""

    save_path = BASE_DIR / sub_dir
    save_path.mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    with mss.mss() as sct:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = os.path.join(save_path, f"screen_{timestamp}.png")
        sct.shot(output=filename)
        return filename