#include "sdaq.h"

byte masterDeviceCode = 0x00;

void connectDevice(byte MASTER_DEVICE_CODE, byte BOARD_TYPE_ID, byte BOARD_NUM)
{
  masterDeviceCode = MASTER_DEVICE_CODE;
  Wire.begin(BOARD_TYPE_ID & BOARD_NUM);
}

void sendBytes(byte SENSOR_ID, byte DATA)
{
  Wire.beginTransmission(masterDeviceCode);
  Wire.write( byte(INFO_MASK | (SENSOR_ID << SENSOR_ID_POS) | (DATA >> (8 - SENSOR_ID_POS))) );
  Wire.write( byte(DATA & DATA_MASK) );
  Wire.endTransmission();
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
