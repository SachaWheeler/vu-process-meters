/* I2C LCD with Arduino example code. More info: https://www.makerguides.com */

// Include the libraries:
// LiquidCrystal_I2C.h: https://github.com/johnrickman/LiquidCrystal_I2C
//#include  // Library for I2C communication
//#include  // Library for LCD
#include <LiquidCrystal_I2C.h>

// Wiring: SDA pin is connected to A4 and SCL pin to A5.
// Connect to LCD via I2C, default address 0x27 (A0-A2 not jumpered)
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);  // Change to (0x27,20,4) for 20x4 LCD.

void setup() {
  Serial.begin(115200);

  pinMode(LED_BUILTIN_TX, INPUT);
  pinMode(LED_BUILTIN_RX, INPUT);
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();

  lcd.setCursor(2, 0);  // Set the cursor on the third column and first row.
  lcd.print("Start demon!");
}

void loop() {

  if (Serial.available() > 0) {
    // Read the incoming data until a newline character is received
    String data = Serial.readStringUntil('\n');

    // Parse the comma-separated values
    float ram = data.substring(0, data.indexOf(',')).toFloat();
    float cpu = data.substring(data.indexOf(',') + 1).toFloat();

    // Display values on the LCD
    lcd.clear();
    lcd.setCursor(3, 0);
    lcd.print("Ram: ");
    lcd.print(ram, 1);
    lcd.print("%");

    lcd.setCursor(3, 1);
    lcd.print("Cpu: ");
    lcd.print(cpu, 1);
    lcd.print("%");
  }
}

/*
#include <LiquidCrystal_I2C.h>

// Define LCD properties
LiquidCrystal_I2C lcd(0x27, 16, 2);  // I2C address 0x27, 16 columns, 2 rows

void setup() {
  // Initialize serial communication and LCD
  Serial.begin(115200);
  lcd.init();
  lcd.begin(16, 2);
  lcd.backlight();  // Turn on the backlight
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming data until a newline character is received
    String data = Serial.readStringUntil('\n');

    // Parse the comma-separated values
    int value1 = data.substring(0, data.indexOf(',')).toInt();
    int value2 = data.substring(data.indexOf(',') + 1).toInt();

    // Display values on the LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Value 1: ");
    lcd.print(value1);

    lcd.setCursor(0, 1);
    lcd.print("Value 2: ");
    lcd.print(value2);
  }
}

*/