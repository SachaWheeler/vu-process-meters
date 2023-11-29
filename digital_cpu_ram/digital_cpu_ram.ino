#include <LiquidCrystal_I2C.h>

// Connect to LCD via I2C, default address 0x27
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);

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

  // turn serial LEDs off
  pinMode(LED_BUILTIN_TX, INPUT);
  pinMode(LED_BUILTIN_RX, INPUT);

  lcd.init();
  lcd.backlight();

  lcd.createChar(1, up_arrow);
  lcd.createChar(2, down_arrow);

  lcd.setCursor(2, 0);  // Set the cursor on the third column and first row.
  lcd.print("Start demon!");
}

bool cleared = false;
bool backlight = true;

void loop() {
  if (Serial.available() > 0) {
    if (cleared == false) {
      lcd.clear();
      cleared = true;
    }

    String data = Serial.readStringUntil('\n');

    int lock = data.substring(0, 1).toInt();
    String line_1 = data.substring(1, data.indexOf(','));
    String line_2 = data.substring(data.indexOf(',') + 1);

    if (lock == 0 && backlight == false) {
      lcd.backlight();
      backlight = true;
    }
    if (lock == 1 && backlight == true){
      lcd.noBacklight();
      backlight = false;
    }

    lcd.setCursor(0, 0);
    lcd.print(line_1);

    lcd.setCursor(0, 1);
    lcd.print(line_2);
  }
}
