HOST = 
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(1)
print ('Socket now listening')


#����
try:
    while True:
        button_input_1 = GPIO.input(33)
        button_input_2 = GPIO.input(40)
           
        #1�� ��ư Ŭ��
        if   button_input_1 == False :
            
            #FCM �˸�
            push_service = FCMNotification(api_key="your key")
            registration_id = "device-token"
            data_message = {"�������� ���������ϴ�" : "Ȯ���� �ּ���"}
            result = push_service.notify_single_device(registration_id=registration_id,data_message=data_message)
            print result
            
            #LED�� ������ �������� ����
            msg = "D i n g   D o n g     D i n g   D o n  g"
            show_message(device, msg, fill="white", font=proportional(CP437_FONT))
            print ('ready')

             #���� ����
            conn, addr = s.accept()
            print("Connected by ", addr)

            #������ ����
            data = conn.recv(1024)
            data = data.decode("utf8").strip()
            print("Received: " + data)
            
            #TTS �ѱ�
            tts_ko(data)
            os.system("omxplayer output.mp3")
            tts_ko("���� ��ư�� ���� �ּ���")
            os.system("omxplayer output.mp3")
            print ('ready')
    

            
        #2�� ��ư Ŭ��
        if  button_input_2 == False :
            # ����
            os.system("arecord -D plughw:1,0 -f S16_LE -c1 -r16000 -d 5 input.wav")
            print("recording complete!")
            
            # STT �ѱ�
            input_kor_str = stt_ko('input.wav')
            print(input_kor_str)
            
            # Ŭ���̾�Ʈ ��������
            
            conn.sendall(input_kor_str.encode("utf-8"))
            conn.close()
            print ('ready')

             #���� ����
            conn, addr = s.accept()
            print("Connected by ", addr)

            #������ ����
            data = conn.recv(1024)
            data = data.decode("utf8").strip()
            print("Received: " + data)
                     
            #TTS �ѱ�
            tts_ko(data)
            os.system("omxplayer output.mp3")
            tts_ko("���� ��ư�� ���� �ּ���")
            os.system("omxplayer output.mp3")
            print ('ready')
            

except KeyboardInterrupt:
    s.close()
    GPIO.cleanup()
