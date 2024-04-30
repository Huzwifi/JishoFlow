# -*- coding: utf-8 -*-
from flox import Flox, ICON_APP_ERROR, FLOW_API, WOX_API
import jisho_api
from urllib.parse import quote
from jisho_api.kanji import Kanji



def generate_jisho_link(kanji):
            base_url = "https://jisho.org/search/"
            encoded_kanji = quote(kanji)
            return [base_url + encoded_kanji]
def jisho_main():
        kanji = input("Enter a kanji character")
        kanji_info = Kanji.request(kanji)
        if kanji_info:
            jisho_link = generate_jisho_link(kanji)
            print("Jisho link:", jisho_link)
        else:
            print("Kanji not found.")



class JishoInput(Flox):
    def query(self, query):
        return [
            {
                "Title": "Enter Kanji here. {}".format(('Your query is: ' + query , query)[query == '']),
                "SubTitle": "Yaay",
                "IcoPath": "icon.png",
                "JsonRPCAction": {
                    "method": "jisho_main",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher"]
                }
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]


if __name__ == "__main__":
    JishoInput()
