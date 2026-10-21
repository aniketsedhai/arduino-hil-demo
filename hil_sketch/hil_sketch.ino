// hil_sketch/hil_sketch.ino
void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd == "PING") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("PONG");
    }
  }
}
