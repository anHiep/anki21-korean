from aqt import gui_hooks
from .model import get_or_create_model
from .autofill import fill_korean_fields

def on_collection_loaded(col):
    get_or_create_model()

def setupButtons(buttons, editor):
    btn = editor.addButton(
        None,
        "AutoFill Korean",
        lambda e=editor: fill_korean_fields(e),
        tip="Auto-fill Korean fields from Naver"
    )
    buttons.append(btn)

def init_addon():
    print("✅ Korean autofill addon initialized.")
    gui_hooks.collection_did_load.append(on_collection_loaded)
    gui_hooks.editor_did_init_buttons.append(setupButtons)
