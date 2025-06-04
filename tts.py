import os
import tempfile
from aqt import mw
from .NaverTTS.navertts.tts import NaverTTS

def save_tts_to_media(word: str) -> str:
    tts = NaverTTS(word, lang='ko')

    with tempfile.NamedTemporaryFile(suffix=f"_{word}_ko.mp3", delete=False) as tmpfile:
        temp_path = tmpfile.name

    tts.save(temp_path)  

    filename_in_media = mw.col.media.add_file(temp_path)

    os.remove(temp_path)

    return filename_in_media
