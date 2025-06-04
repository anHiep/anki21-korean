# KoreanCard - Anki Add-on for Korean Vocabulary

**KoreanCard** is an Anki add-on that helps you create Korean vocabulary cards with automatic filling of pronunciation, Korean and English meanings, and Korean TTS audio.

---

## Features

- Automatically creates a custom Korean note type with fields for:
  - Korean word
  - Sound (Korean TTS audio)
  - Korean definition
  - English word
  - English definition
- Fetches definitions and translations using the official [KRDict API](https://krdict.korean.go.kr).
- Generates Korean TTS audio using the [NaverTTS](https://github.com/scottgigante/NaverTTS/tree/3f8507ec3dfc832d252d191981ec84bf01c1da13) library.
- Adds a button in the Anki editor to autofill fields from your input Korean word.

---

## TTS Source

This add-on uses the [NaverTTS](https://github.com/scottgigante/NaverTTS/tree/3f8507ec3dfc832d252d191981ec84bf01c1da13) project for text-to-speech synthesis of Korean words.  
The TTS module is bundled internally and used to generate pronunciation audio files stored in Anki's media collection.

---

## How to Use

### 1. Add the KoreanCard Note Type

- Open Anki.
- In the editor, create a **new card** and select the **KoreanCard** note type.
- If the note type does not exist yet, the add-on will automatically create it for you with all necessary fields and card templates.

### 2. Add Your Korean Word

- Enter a Korean word in the **Korean** field.
- Click the **AutoFill Korean** button added by the add-on in the editor toolbar.
- The add-on will fetch Korean and English definitions, and automatically generate Korean TTS audio linked in the **Sound** field.
- Your card is now ready to be reviewed!

---

## Configuration: Setting Your Own KRDict API Key

By default, the add-on uses a shared API key to fetch data from the Korean dictionary API.  
For reliability and to avoid rate limits, you may want to use your own API key.

### Steps to add your own API key:

1. Open the file `config.py` inside the add-on folder.
2. Find the `api_key` entry.
3. Replace the existing value with your own API key from [KRDict API](https://krdict.korean.go.kr/).
4. Save the file and restart Anki.

Example snippet from `config.py`:

```python
KRDICT_API_KEY = "{YOUR_API}"
