from urllib.parse import quote


def encode_uri(to_encode: str) -> str:
    return quote(to_encode, safe="~()*!.'")
