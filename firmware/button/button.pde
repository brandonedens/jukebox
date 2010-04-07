/*
 * Arcade Button Test
 *
 */


/******************************************************************************
 * Defines
 */

#define LED_PIN 13
#define BUTTON_WHITE 2
#define BUTTON_BLUE 3
#define BUTTON_GREEN 4
#define BUTTON_PURPLE 5
#define BUTTON_YELLOW 6
#define BUTTON_RED 7
#define COIN 14

/******************************************************************************
 * Global Variables
 */
int button_white;
int button_blue;
int button_green;
int button_purple;
int button_yellow;
int button_red;
int coin;

/******************************************************************************
 * Functions
 */


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

    /* Set initial state of all buttons and coin. */
    button_white = digitalRead(BUTTON_WHITE);
    button_blue = digitalRead(BUTTON_BLUE);
    button_green = digitalRead(BUTTON_GREEN);
    button_purple = digitalRead(BUTTON_PURPLE);
    button_yellow = digitalRead(BUTTON_YELLOW);
    button_red = digitalRead(BUTTON_RED);
    coin = digitalRead(COIN);
}

/** Print the value of a single button. */
void print_button(int button_value)
{
    if (button_value == HIGH) {
        Serial.print("1");
    } else {
        Serial.print("0");
    }
}

/** Iterate over state of buttons printing their values. */
void print_buttons()
{
    Serial.print("Juke");
    print_button(button_blue);
    print_button(button_green);
    print_button(button_purple);
    print_button(button_red);
    print_button(button_white);
    print_button(button_yellow);
    print_button(coin);
}

void loop()
{
    int tmp;
    bool changed = false;

    /* Iterate over all buttons reading their state and if new state is
     * detected then we will finally print the state of the buttons.
     */
    tmp = digitalRead(BUTTON_WHITE);
    if (tmp != button_white) {
        button_white = tmp;
        changed = true;
    }

    tmp = digitalRead(BUTTON_BLUE);
    if (tmp != button_blue) {
        button_blue = tmp;
        changed = true;
    }

    tmp = digitalRead(BUTTON_GREEN);
    if (tmp != button_green) {
        button_green = tmp;
        changed = true;
    }

    tmp = digitalRead(BUTTON_PURPLE);
    if (tmp != button_purple) {
        button_purple = tmp;
        changed = true;
    }

    tmp = digitalRead(BUTTON_YELLOW);
    if (tmp != button_yellow) {
        button_yellow = tmp;
        changed = true;
    }

    tmp = digitalRead(BUTTON_RED);
    if (tmp != button_red) {
        button_red = tmp;
        changed = true;
    }

    tmp = digitalRead(COIN);
    if (tmp != coin) {
        coin = tmp;
        changed = true;
    }

    if (changed) {
        print_buttons();
    }
}
