from pathlib import Path
from urllib.parse import quote
import webbrowser
from jisho_api import kanji

from jisho_api import kanji
from urllib.parse import quote

class JishoFlow:
    kanji = input("Enter kanji here:")
    BASE_URL = "https://jisho.org/search/"
    ENCODED_KANJI = quote(kanji)
    GENERATED_LINK = BASE_URL + ENCODED_KANJI

    kanji = input("Enter kanji here:")

    def open_url(self, GENERATED_LINK):
         webbrowser.open(GENERATED_LINK)

         
if __name__ == "__main__":
    JishoFlow()
