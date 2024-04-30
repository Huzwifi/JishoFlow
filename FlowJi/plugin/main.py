from flox import Flox, ICON_APP_ERROR, FLOW_API, WOX_API

import jisho_api
from urllib.parse import quote
from jisho_api.kanji import Kanji


def generate_jisho_link(kanji):
    base_url = "https://jisho.org/search/"
    encoded_kanji = quote(kanji)
    return base_url + encoded_kanji



def main():
    kanji = input("Enter a kanji character: ")
    kanji_info = Kanji.request(kanji)
    if kanji_info:
        jisho_link = generate_jisho_link(kanji)
        print("Jisho link:", jisho_link)
    else:
        print("Kanji not found.")


if __name__ == "__main__":
    main()


