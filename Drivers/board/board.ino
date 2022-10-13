#include "sdaq.h"

// Turn this off when you want less overhead
#define SERIAL_OUTPUT_ENABLED true

/* BOARD CONSTANTS */
#define BOARD_TYPE    (ADC_BOARD)
    // Translation: First ADC board on main RPI stack

int I2C_ADDRESS = 0;

void setup()
{
  I2C_ADDRESS = (BOARD_TYPE | getBoardID());
  
  serialBegin(SERIAL_OUTPUT_ENABLED);
  connectDevice(I2C_ADDRESS);

  setupBoard();
}

int i = 0;

int getBoardID()
{
  return 0;
  
  pinMode(0, INPUT);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);

  int id = digitalRead(3) << 2;
  id += digitalRead(2);
  id << 2;
  id += digitalRead(1);
  id << 2;
  id += digitalRead(0);
  return id;
}

void requestEvent()
{
  Wire.write( byte(I2C_ADDRESS) );
  uint16_t val = (uint16_t)(analogRead(A0));
  #define WRITE_SHORTMULTI(value, func) func(byte(value)); func(byte(value >> 8))
  WRITE_SHORTMULTI(val, Wire.write);
  val = (uint16_t)(analogRead(A1));
  WRITE_SHORTMULTI(val, Wire.write);
  val = (uint16_t)(analogRead(A2));
  WRITE_SHORTMULTI(val, Wire.write);
  val = (uint16_t)(analogRead(A3));
  WRITE_SHORTMULTI(val, Wire.write);

  Wire.write( byte(digitalRead(2)) );
  Wire.write( byte(digitalRead(3)) );
  Wire.write( byte(digitalRead(4)) );
  Wire.write( byte(digitalRead(5)) );
  #undef WRITE_SHORTMULTI
}

void setupBoard()
{
  analogReference(DEFAULT);
  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
}

void loop() {}
