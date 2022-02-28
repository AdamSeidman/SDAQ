#include "sdaq.h"

void connectDevice(byte BOARD_TYPE_ID, byte BOARD_NUM)
{
  // IDs should be 0-7
  Wire.begin(BOARD_TYPE_ID | BOARD_NUM);
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
