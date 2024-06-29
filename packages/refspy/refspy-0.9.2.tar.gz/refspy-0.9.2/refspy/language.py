from typing import Dict, List

from pydantic import BaseModel

from refspy.languages.english import ENGLISH


class Language(BaseModel):
    verse_markers: List[str]
    number_prefixes: Dict[str, List[str]]


# Use the first two chars of locale strings for languages:
LANGUAGES = {
    "en": ENGLISH,
}


def get_language(name: str) -> Language:
    if name in LANGUAGES:
        return LANGUAGES[name]
    else:
        raise ValueError(f"Language '{name}' not found.")
