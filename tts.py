from .NaverTTS.navertts.tts import NaverTTS
import os
from aqt import mw

def save_tts_to_media(word: str) -> str:
    tts = NaverTTS(word, lang='ko')
    temp_path = f"{word}_ko.mp3"
    tts.save(temp_path)
    filename_in_media = mw.col.media.add_file(temp_path)
    os.remove(temp_path)
    return filename_in_media
