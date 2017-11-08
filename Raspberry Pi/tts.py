# -*- coding: utf-8 -*-

from gtts import gTTS
import os
import sys


def tts_ko(text):
    tts = gTTS(text, lang='ko')
    tts.save("output.mp3")
    
if __name__ == '__main__':
    
    #한글사용 문자열 인코딩 변경
    reload(sys)
    sys.setdefaultencoding('utf-8')

    text = raw_input("문자를 입력하세요: ")
    tts_ko(text)

    os.system("omxplayer output.mp3")