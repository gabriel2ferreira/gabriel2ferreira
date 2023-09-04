//Summary
const int sensorPin = A0;  // Pino analógico onde o módulo KY-013 está conectado

void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  while (!Serial) {
    // Aguarda até que a comunicação serial seja estabelecida
  }
}

void loop() {
  // Leitura da tensão no pino analógico
  int sensorValue = analogRead(sensorPin);

  // Imprime a leitura no Serial Monitor
  Serial.print("Tensao lida: ");
  Serial.print(sensorValue);
  Serial.println(" (0-1023)");

  // Aguarda 2 segundos antes de fazer a próxima leitura
  delay(2000);
}
