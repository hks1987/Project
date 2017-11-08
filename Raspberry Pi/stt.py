# -*- coding: utf-8 -*-
import io
import sys
import os
import json
from google.cloud import speech

def stt_ko(speech_file):
    """Transcribe the given audio file."""
    
    speech_client = speech.Client()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
            content=content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate_hertz=16000)

    alternatives = audio_sample.recognize('ko-KR')
	
	
    for alternative in alternatives:
	return alternative.transcript
	
if __name__ == '__main__':
    
		
    # 인증 환경 변수 설정
    #os.system("export GOOGLE_APPLICATION_CREDENTIALS=your key")
    # 위 환경변수 명령어는 자식 프로세스에서는 가능하지않다. 
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your key"
		
    # 인코딩 설정
    reload(sys)
    sys.setdefaultencoding('utf-8')
		
    # 녹음
    os.system("arecord -D plughw:1,0 -f S16_LE -c1 -r16000 -d 3 input.wav")
    print("recording complete!")
	
    # STT 한글
    input_kor_str = stt_ko('input.wav')
    print(input_kor_str)



