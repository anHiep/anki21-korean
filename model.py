from aqt import mw

MODEL_NAME = "KoreanCard"
FIELDS = ["Korean", "Sound", "Korean Definition", "English", "English Definition"]

def get_or_create_model():
    col = mw.col
    if not col:
        return

    model = col.models.by_name(MODEL_NAME)
    if model:
        return model

    model = col.models.new(MODEL_NAME)

    for field_name in FIELDS:
        fld = col.models.new_field(field_name)
        col.models.addField(model, fld)

    recognition = col.models.new_template("Recognition")
    recognition["qfmt"] = "{{Korean}}<br><div style='display:none'>{{Sound}}</div>"
    recognition["afmt"] = (
        "{{FrontSide}}<hr><br>"
        "<br>{{English}}<br><br><br>"
        "<b onclick=\"this.nextElementSibling.style.display = (this.nextElementSibling.style.display === 'none') ? 'block' : 'none';\" style='cursor:pointer; color:gray;'>English Definition</b>"
        "<div style='display:none;'>{{English Definition}}</div><br><br>"
        "<b onclick=\"this.nextElementSibling.style.display = (this.nextElementSibling.style.display === 'none') ? 'block' : 'none';\" style='cursor:pointer; color:gray;'>Korean Definition</b>"
        "<div style='display:none;'>{{Korean Definition}}</div>"
    )

    recall = col.models.new_template("Recall")
    recall["qfmt"] = "{{English}}"
    recall["afmt"] = (
        "{{FrontSide}}<hr><br>"
        "<br>{{Korean}}<br><br><br>"
        "<b onclick=\"this.nextElementSibling.style.display = (this.nextElementSibling.style.display === 'none') ? 'block' : 'none';\" style='cursor:pointer; color:gray;'>Korean Definition</b>"
        "<div style='display:none;'>{{Korean Definition}}</div><br><br>"
        "<b onclick=\"this.nextElementSibling.style.display = (this.nextElementSibling.style.display === 'none') ? 'block' : 'none';\" style='cursor:pointer; color:gray;'>English Definition</b>"
        "<div style='display:none;'>{{English Definition}}</div><br><br>"
        "<div style='display:none'>{{Sound}}</div>"
    )

    col.models.addTemplate(model, recognition)
    col.models.addTemplate(model, recall)
    col.models.save(model)
    mw.requireReset()

    return model
