/* I2C LCD with Arduino example code. More info: https://www.makerguides.com */

// Include the libraries:
// LiquidCrystal_I2C.h: https://github.com/johnrickman/LiquidCrystal_I2C
//#include  // Library for I2C communication
//#include  // Library for LCD
#include <LiquidCrystal_I2C.h>

// Wiring: SDA pin is connected to A4 and SCL pin to A5.
// Connect to LCD via I2C, default address 0x27 (A0-A2 not jumpered)
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);  // Change to (0x27,20,4) for 20x4 LCD.

byte up_arrow[8] = {
  B00100,
  B01110,
  B10101,
  B00100,
  B00100,
  B00100,
  B00100,
};

byte down_arrow[8] = {
  B00100,
  B00100,
  B00100,
  B00100,
  B10101,
  B01110,
  B00100,
};

void setup() {
  Serial.begin(115200);

  pinMode(LED_BUILTIN_TX, INPUT);
  pinMode(LED_BUILTIN_RX, INPUT);
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();

  lcd.createChar(0, up_arrow);
  lcd.createChar(1, down_arrow);

  lcd.setCursor(2, 0);  // Set the cursor on the third column and first row.
  lcd.print("Start demon!");
}

void loop() {

  if (Serial.available() > 0) {
    // Read the incoming data until a newline character is received
    String data = Serial.readStringUntil('\n');

    // Parse the comma-separated values
    String line_1 = data.substring(0, data.indexOf(','));
    String line_2 = data.substring(data.indexOf(',') + 1);

    // Display values on the LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(line_1);

    lcd.setCursor(0, 1);
    lcd.print(line_2);

    lcd.setCursor(8, 0);
    lcd.write((byte)0);  // Display the up_arrow character

    lcd.setCursor(8, 1);
    lcd.write((byte)1);  // Display the down_arrow character
  }
}
