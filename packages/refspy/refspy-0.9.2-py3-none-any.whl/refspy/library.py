from typing import List

from pydantic import BaseModel

from refspy.libraries.en_US import DC, DC_ORTHODOX, NT, OT
from refspy.book import Book


class Library(BaseModel):
    id: int
    name: str
    abbrev: str
    code: str
    books: List[Book]


LIBRARIES = {
    "protestant": {"en_US": [OT, NT]},
    "catholic": {"en_US": [OT, DC, NT]},
    "orthodox": {"en_US": [OT, DC, DC_ORTHODOX, NT]},
}


def get_library(name: str, locale: str) -> List[Library]:
    if name in LIBRARIES:
        if locale in LIBRARIES[name]:
            return LIBRARIES[name][locale]
    raise ValueError(f"Library '{name}' not found for locale '{locale}'.")
