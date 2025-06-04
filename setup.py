import os

def main():
    print("Setup KoreanCard Anki Add-on")

    api_key = input("Please enter your KRDICT_API_KEY (get one from https://krdict.korean.go.kr/): ").strip()
    if not api_key:
        print("API key is required. Exiting.")
        return

    # Path to the add-on config file to write the key
    config_path = os.path.join(os.path.dirname(__file__), "config.py")

    # Write the API key to config.py
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(f'KRDICT_API_KEY = "{api_key}"\n')

    print(f"API key saved to {config_path}.\nYou can now use the add-on with your key.")

if __name__ == "__main__":
    main()
