#define sensorPin A0
#define ledPin 13  // Pin to control the LED (simulates water pump)

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  // Initially, the LED is off
  Serial.begin(9600);  // Communication with Python
}

void loop() {
  int sensorValue = readSensor();
  int active = 0;

  if (sensorValue <= 80 && active == 0) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  // Send sensor value as JSON to Python
  Serial.println("{\"sensorValue\": " + String(sensorValue) + "}");


  // Check for incoming commands from Python
  if (Serial.available() > 0) {
    String command = Serial.readString();
    command.trim();  // Remove any extraneous characters

    if (command == "WATER_ON") {
      digitalWrite(ledPin, HIGH);  // Turn on LED (activate water pump)
      active = 1;
    } else if (command == "WATER_OFF") {
      active = 0;
      digitalWrite(ledPin, LOW);   // Turn off LED (deactivate water pump)
    }
  }

  delay(1000);
}

int readSensor() {
  delay(500);
  int sensorValue = analogRead(sensorPin);
  int outputValue = map(sensorValue, 0, 1023, 255, 0);  // Map to 8-bit value
  return outputValue;
}
