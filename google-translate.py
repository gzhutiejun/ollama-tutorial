# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

async def tranlate_text():
    translator = Translator()
    text_to_translate = translator.translate("取款交易", src="zh-cn", dest="en")
    translated_text = text_to_translate.text

tranlate_text()
