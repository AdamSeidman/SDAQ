#include "sdaq.h"

// Turn this off when you want less overhead
#define SERIAL_OUTPUT_ENABLED true

/* BOARD CONSTANTS */
#define BOARD_ID    (0x01)
#define BOARD_TYPE  (ADC_BOARD)
#define MASTER_ADDR (RPI_DEVC_CODE)
    // Translation: First ADC board on main RPI stack

void setup()
{
  serialBegin(SERIAL_OUTPUT_ENABLED);
  connectDevice(MASTER_ADDR, BOARD_TYPE, BOARD_ID);
}

void loop() { // TODO
  sendBytes(1, 32);
  sendBytes(2, 16);
  _println("H");
  delay(1000);

  sendBytes(1, 33);
  sendBytes(2, 17);
  _println("i");
  delay(1000);
}
