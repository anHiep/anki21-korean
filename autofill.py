from aqt import mw
from aqt.editor import Editor
from aqt.qt import QMessageBox
from .model import MODEL_NAME, FIELDS
from .krdict import fetch_from_krdict
from .tts import save_tts_to_media

def fill_korean_fields(editor: Editor):
    note = editor.note
    if not note or note.model().get('name') != MODEL_NAME:
        QMessageBox.warning(editor.parentWindow, "Wrong Note Type", f"Please select a note of type '{MODEL_NAME}'.")
        return

    korean_text = note[FIELDS[0]].strip()
    if not korean_text:
        QMessageBox.information(editor.parentWindow, "No Korean Word", "Please enter a Korean word in the 'Korean' field first.")
        return

    data = fetch_from_krdict(korean_text)

    audio_filename = save_tts_to_media(data["word"])

    note[FIELDS[0]] = data["word"]
    note[FIELDS[1]] = f"[sound:{audio_filename}]"
    note[FIELDS[2]] = data["definition_kr"]
    note[FIELDS[3]] = data["translation_word"]
    note[FIELDS[4]] = data["translation_def"]

    editor.loadNote()

