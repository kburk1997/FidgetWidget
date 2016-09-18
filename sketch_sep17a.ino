#include <Wire.h>

int button1=0;
int button2=0;
int button3=0;

int lightValue=500;

int number=0;
int state=0;

#define SLAVE_ADDRESS 0x04

void setup() {
    Serial.begin(9600);
  // put your setup code here, to run once:
  //Pushbutton inputs
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  pinMode(8, INPUT);
  
  //initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  //define callbacks for i2c
  
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  button1=digitalRead(13);
  button2=digitalRead(12);
  button3=digitalRead(8);

  Serial.println(button1);
  
  //Send button1
  if(!button1 || !button2 || !button3){
    number=0;
    sendData();
    //Wait until all buttons are released
    while(!button1 || !button2 || !button3){
    }
  }
  
  lightValue=analogRead(A0);
  if(lightValue <450 || lightValue >550){
   number=lightValue/100;
    sendData(); 
  }
  
  //
}

void receiveData(int byteCount){
  while(Wire.available()){
    number=Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
    
    if(number==1){
      if (state==0){
        state=1;
      }
      else{
        state=0;
      }
    }
  }
}

void sendData(){
  Wire.write(number);
}
