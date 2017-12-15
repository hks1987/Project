
public class MainActivity extends AppCompatActivity {
    TextView recieveText,textIp,textPort;
    EditText messageText;
    Button connectBtn, clearBtn;

    Socket socket = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().setElevation(0);
        FirebaseInstanceId.getInstance().getToken();

        connectBtn = (Button) findViewById(R.id.buttonConnect);
        clearBtn = (Button) findViewById(R.id.buttonClear);
        textIp = (TextView) findViewById(R.id.text_ip);
        textPort = (TextView) findViewById(R.id.text_port);
        recieveText = (TextView) findViewById(R.id.textViewReciev);
        messageText = (EditText) findViewById(R.id.messageText);


        Intent intent = getIntent();
        String ip = intent.getStringExtra("IP");
        String port = intent.getStringExtra("PORT");

        textIp.setText(ip);
        textPort.setText(port);

        //connect 버튼 클릭
        connectBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MyClientTask myClientTask = new MyClientTask(textIp.getText().toString(), Integer.parseInt(textPort.getText().toString()), messageText.getText().toString());
                myClientTask.execute();
                //messageText.setText("");
            }
        });

        //clear 버튼 클릭
        clearBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                recieveText.setText("");
                messageText.setText("");
            }
        });


        WebView webView = (WebView)findViewById(R.id.webView);
        webView.setWebViewClient(new WebViewClient());
        webView.setBackgroundColor(255);

        webView.getSettings().setLoadWithOverviewMode(true);
        webView.getSettings().setUseWideViewPort(true);

        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        webView.loadData("<html><head><style type='text/css'>body{margin:auto auto;text-align:center;} img{width:100%25;} div{overflow: hidden;} </style></head><body><img src='http://192.168.0.4:8080/stream/video.mjpeg'/></div></body></html>","text/html","UTF-8");


    }

    public class MyClientTask extends AsyncTask<Void,Void,Void>{
        String dstAddress;
        int dstPort;
        String response = "";
        String myMessage = "";

        //constructor
        MyClientTask(String addr, int port, String message){
            dstAddress = addr;
            dstPort = port;
            myMessage = message;
        }
        @Override
            protected Void doInBackground(Void...arg0){
                Socket socket =null;
                myMessage = myMessage.toString();
                try{
                    socket = new Socket(dstAddress,dstPort);
                    //송신
                    OutputStream out = socket.getOutputStream();
                    out.write(myMessage.getBytes());

                    //수신

                    ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(1024);
                    byte[] buffer = new byte[1024];
                    int bytesRead;
                    InputStream inputStream = socket.getInputStream();

                    while((bytesRead = inputStream.read(buffer)) != -1){
                        byteArrayOutputStream.write(buffer,0,bytesRead);
                        response += byteArrayOutputStream.toString("UTF-8");
                    }
                    response = "서버의 응답 : " + response;
                }catch(UnknownHostException e){
                    e.printStackTrace();
                    response = "UnknownHostException: "+e.toString();
                }catch(IOException e){
                    e.printStackTrace();
                    response = "IOException:"+e.toString();
                }finally{
                    if(socket != null){
                        try{
                            socket.close();
                        }catch(IOException e){
                            e.printStackTrace();
                        }
                    }
                }
                return null;
        }
        @Override
        protected void onPostExecute(Void result){
            recieveText.setText(response);
            super.onPostExecute(result);
        }
    }
}
