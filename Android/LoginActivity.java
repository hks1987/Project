

public class LoginActivity extends AppCompatActivity {
    EditText edit1, edit2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);


        Button button = (Button) findViewById(R.id.btncon);
        edit1 = (EditText) findViewById(R.id.etip);
        edit2 = (EditText) findViewById(R.id.etport);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in = new Intent(LoginActivity.this, MainActivity.class);
                in.putExtra("IP",edit1.getText().toString());
                in.putExtra("PORT",edit2.getText().toString());
                startActivity(in);
            }
        });
    }
}
