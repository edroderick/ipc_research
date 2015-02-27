/*
 Serial1 : Dynamixel_Poart
 Serial2 : Serial_Poart(4pin_Molex)
 Serial3 : Serial_Poart(pin26:Tx3, pin27:Rx3)
 
 TxD3(Cm9_Pin26) <--(Connect)--> RxD(PC)
 RxD3(Cm9_Pin27) <--(Connect)--> TxD(PC)
 */

char inChar;
byte index = 0;

void setup() {
  Serial3.begin(9600);
}

void loop() {
 
  //while(Serial3.available() == 0){}  //block untill serial available
  while(SerialUSB.available() == 0){}  //block untill serial available
  //if (Serial3.available() > 0){
  if (SerialUSB.available() > 0){
    //while(Serial3.available() > 0) {
    while(SerialUSB.available() > 0) {
      char inData[20];
      //while(Serial3.available()>0){
      while(SerialUSB.available()>0){
        if(index < 19){
          //inChar = Serial3.read(); //read a character
          inChar = SerialUSB.read(); //read a character
          inData[index] = inChar;
          index++;
          inData[index] = '\0';
        }
       }
      SerialUSB.print(inData[0]);
    }
  index = 0;
}
}

