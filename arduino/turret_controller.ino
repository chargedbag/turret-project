#include <Servo.h>

Servo panServo;
Servo tiltServo;

String input = "";
bool complete = false;

void setup() {
  Serial.begin(115200);

  panServo.attach(9);
  tiltServo.attach(10);

  panServo.write(90);
  tiltServo.write(90);
}

void loop() {
  if (complete) {
    int comma = input.indexOf(',');

    if (comma > 0) {
      int pan = input.substring(0, comma).toInt();
      int tilt = input.substring(comma + 1).toInt();

      pan = constrain(pan, 0, 180);
      tilt = constrain(tilt, 0, 180);

      panServo.write(pan);
      tiltServo.write(tilt);
    }

    input = "";
    complete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char c = (char)Serial.read();

    if (c == '\n') {
      complete = true;
    } else {
      input += c;
    }
  }
}
