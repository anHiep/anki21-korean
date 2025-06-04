import requests
from bs4 import BeautifulSoup
from .config import KRDICT_API_KEY

def fetch_from_krdict(word):
    result = {
        "word": "", "sound_url": "", "definition_kr": "",
        "translation_word": "", "translation_def": "",
    }
    url = (
        f"https://krdict.korean.go.kr/api/search?"
        f"key={KRDICT_API_KEY}&q={word}&translated=y&trans_lang=1&req_type=xml"
    )

    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "xml")
        item = soup.find("item")
        if not item:
            return result

        result["word"] = item.find("word").text if item.find("word") else ""
        sense = item.find("sense")
        if sense:
            result["definition_kr"] = sense.find("definition").text if sense.find("definition") else ""
            translation = sense.find("translation")
            if translation:
                result["translation_word"] = translation.find("trans_word").text if translation.find("trans_word") else ""
                result["translation_def"] = translation.find("trans_dfn").text if translation.find("trans_dfn") else ""

    except Exception as e:
        print(f"KRDICT fetch error: {e}")

    return result
