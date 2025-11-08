# cipher.py
import base64

def b64_to_bytes(s: str) -> bytes:
    """
    Returns bytes; note: s may contain accidental newlines/spaces.
    """
    if isinstance(s, str):
        # strip trailing whitespace/newlines but preserve internal whitespace
        s = s.strip()
        return base64.b64decode(s)
    return base64.b64decode(s)

def bytes_to_text(b: bytes) -> str:
    # decode using utf-8, but be defensive about bytes that might include nulls
    return b.decode("utf-8").strip("\x00")
