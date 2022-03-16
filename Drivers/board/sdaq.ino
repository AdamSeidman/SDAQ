#include "sdaq.h"

void connectDevice(byte i2c_address)
{
  // IDs should be 0-7
  Wire.setClock(I2C_RATE);
  Wire.begin(i2c_address);
  Wire.onRequest(requestEvent);
}

boolean SERIAL_OUTPUT_ALLOWED = false;

void serialBegin(boolean OUTPUT_ENABLED)
{
  if (OUTPUT_ENABLED)
  {
    Serial.begin(BAUD_RATE);
    SERIAL_OUTPUT_ALLOWED = true;
    _println("Welcome!");
  }
}

void _println(String s)
{
  if (SERIAL_OUTPUT_ALLOWED)
  {
    Serial.println(s);
  }
}

void _print(String s)
{
  if (SERIAL_OUTPUT_ALLOWED)
  {
    Serial.print(s);
  }
}
