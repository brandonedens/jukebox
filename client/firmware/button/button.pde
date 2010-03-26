/*
 * Arcade Button Test
 *
 */

#define LED_PIN 13
#define BUTTON_WHITE 2
#define BUTTON_BLUE 3
#define BUTTON_GREEN 4
#define BUTTON_PURPLE 5
#define BUTTON_YELLOW 6
#define BUTTON_RED 7
#define COIN 14


void setup()
{
    Serial.begin(115200);
    pinMode(BUTTON_WHITE, INPUT);
    pinMode(BUTTON_BLUE, INPUT);
    pinMode(BUTTON_GREEN, INPUT);
    pinMode(BUTTON_PURPLE, INPUT);
    pinMode(BUTTON_YELLOW, INPUT);
    pinMode(BUTTON_RED, INPUT);
    pinMode(COIN, INPUT);
    //digitalWrite(COIN, HIGH);

    pinMode(LED_PIN, OUTPUT);
}

void loop()
{
    Serial.print("Juke");

    if (digitalRead(BUTTON_WHITE) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(BUTTON_BLUE) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(BUTTON_GREEN) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(BUTTON_PURPLE) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(BUTTON_YELLOW) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(BUTTON_RED) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }

    if (digitalRead(COIN) == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }
    delay(50);
}
