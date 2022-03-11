#include "sdaq.h"

// Turn this off when you want less overhead
#define SERIAL_OUTPUT_ENABLED true

/* BOARD CONSTANTS */
#define BOARD_ID      (0x01)
#define BOARD_TYPE    (ADC_BOARD)
    // Translation: First ADC board on main RPI stack

#define I2C_ADDRESS   BOARD_ID | BOARD_TYPE 

void setup()
{
  serialBegin(SERIAL_OUTPUT_ENABLED);
  connectDevice(I2C_ADDRESS);

  setupBoard();
}

int i = 0;

void requestEvent()
{
  Wire.write( byte(I2C_ADDRESS) );
  
  Wire.write( byte(analogRead(A0)) );
  Wire.write( byte(analogRead(A1)) );
  Wire.write( byte(analogRead(A2)) );
  Wire.write( byte(analogRead(A3)) );

  Wire.write( byte(digitalRead(2)) );
  Wire.write( byte(digitalRead(3)) );
  Wire.write( byte(digitalRead(4)) );
  Wire.write( byte(digitalRead(5)) );
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
