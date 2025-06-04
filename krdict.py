import os
import requests
import xml.etree.ElementTree as ET

def fetch_from_krdict(word):
    result = {
        "word": "", "sound_url": "", "definition_kr": "",
        "translation_word": "", "translation_def": "",
    }

    KRDICT_API_KEY = os.environ.get("KRDICT_API_KEY")
    if not KRDICT_API_KEY:
        raise ValueError("KRDICT_API_KEY not set")

    url = (
        f"https://krdict.korean.go.kr/api/search?"
        f"key={KRDICT_API_KEY}&q={word}&translated=y&trans_lang=1&req_type=xml"
    )

    res = requests.get(url)
    res.raise_for_status()

    root = ET.fromstring(res.text)

    item = root.find("item")
    if item is None:
        return result

    word_node = item.find("word")
    if word_node is not None:
        result["word"] = word_node.text or ""

    sense = item.find("sense")
    if sense is not None:
        def_node = sense.find("definition")
        if def_node is not None:
            result["definition_kr"] = def_node.text or ""

        translation = sense.find("translation")
        if translation is not None:
            trans_word = translation.find("trans_word")
            trans_def = translation.find("trans_dfn")
            if trans_word is not None:
                result["translation_word"] = trans_word.text or ""
            if trans_def is not None:
                result["translation_def"] = trans_def.text or ""

    return result