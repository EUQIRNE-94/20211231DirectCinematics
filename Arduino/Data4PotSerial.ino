
int lectura[4] = {0,0,0,0};
float salida[4];
float EMA_a = 0.01;
static const uint8_t analog_pins[] = {A0,A1,A2,A3};
long int t,tant=0;
float dt = 10;
void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);
  Serial.begin(115200);
  for(int i = 0;i<4;i++){
    salida[i] = analogRead(analog_pins[i]);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  t = millis();
  for(int i = 0;i<4;i++){
    lectura[i] = analogRead(analog_pins[i]);
    salida[i] = (EMA_a*lectura[i]) + ((1-EMA_a)*salida[i]);
  }

  if(t-tant >= dt){
    Serial.print(t);
    Serial.print(",");
    for(int i=0;i<4;i++){
      Serial.print(salida[i]);
      if(i<3){
        Serial.print(",");
      }
    }
    Serial.println();
    tant = t;
  }
}
