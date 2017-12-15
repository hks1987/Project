HOST = 
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(1)
print ('Socket now listening')


#메인
try:
    while True:
        button_input_1 = GPIO.input(33)
        button_input_2 = GPIO.input(40)
           
        #1번 버튼 클릭
        if   button_input_1 == False :
            
            #FCM 알림
            push_service = FCMNotification(api_key="your key")
            registration_id = "device-token"
            data_message = {"초인종이 눌러졌습니다" : "확인해 주세요"}
            result = push_service.notify_single_device(registration_id=registration_id,data_message=data_message)
            print result
            
            #LED는 끝나야 다음구문 시작
            msg = "D i n g   D o n g     D i n g   D o n  g"
            show_message(device, msg, fill="white", font=proportional(CP437_FONT))
            print ('ready')

             #접속 승인
            conn, addr = s.accept()
            print("Connected by ", addr)

            #데이터 수신
            data = conn.recv(1024)
            data = data.decode("utf8").strip()
            print("Received: " + data)
            
            #TTS 한글
            tts_ko(data)
            os.system("omxplayer output.mp3")
            tts_ko("녹음 버튼을 눌러 주세요")
            os.system("omxplayer output.mp3")
            print ('ready')
    

            
        #2번 버튼 클릭
        if  button_input_2 == False :
            # 녹음
            os.system("arecord -D plughw:1,0 -f S16_LE -c1 -r16000 -d 5 input.wav")
            print("recording complete!")
            
            # STT 한글
            input_kor_str = stt_ko('input.wav')
            print(input_kor_str)
            
            # 클라이언트 문자전달
            
            conn.sendall(input_kor_str.encode("utf-8"))
            conn.close()
            print ('ready')

             #접속 승인
            conn, addr = s.accept()
            print("Connected by ", addr)

            #데이터 수신
            data = conn.recv(1024)
            data = data.decode("utf8").strip()
            print("Received: " + data)
                     
            #TTS 한글
            tts_ko(data)
            os.system("omxplayer output.mp3")
            tts_ko("녹음 버튼을 눌러 주세요")
            os.system("omxplayer output.mp3")
            print ('ready')
            

except KeyboardInterrupt:
    s.close()
    GPIO.cleanup()
