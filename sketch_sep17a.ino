int button1=0;
int button2=0;
int button3=0;
int lightValue=0;

void setup() {
    Serial.begin(9600);
  // put your setup code here, to run once:
  //Pushbutton inputs
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  pinMode(8, INPUT);
  
  //Set up analog input
  
}

void loop() {
  // put your main code here, to run repeatedly:
  button1=digitalRead(13);
  button2=digitalRead(12);
  button3=digitalRead(8);
  lightValue=analogRead(A0);
  Serial.println(lightValue);
}
