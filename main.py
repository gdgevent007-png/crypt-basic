# main.py
# Slight twist: imports intentionally named differently in cipher module to force checking
from cipher import b64_to_bytes, bytes_to_text

def main():
    with open("secret.txt", "r", encoding="utf-8") as f:
        payload = f.read()  # may include newline at end

    # subtle issue: previously code used base64 decode on bytes vs str incorrectly
    raw = b64_to_bytes(payload)
    text = bytes_to_text(raw)
    # ensure uppercase (the solution expects uppercase)
    print(text.upper())

if __name__ == "__main__":
    main()
