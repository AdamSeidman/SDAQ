#include "sdaq.h"

// Turn this off when you want less overhead
#define SERIAL_OUTPUT_ENABLED true

/* BOARD CONSTANTS */
#define BOARD_ID    (0x01)
#define BOARD_TYPE  (ADC_BOARD)
#define MASTER_ADDR (RPI_DEVC_CODE)
    // Translation: First ADC board on main RPI stack

void recvEvent(int numBytes);
void reqEvent();

void setup()
{
  serialBegin(SERIAL_OUTPUT_ENABLED);
  connectDevice(MASTER_ADDR, BOARD_TYPE, BOARD_ID);
  Wire.onRequest(reqEvent);
  Wire.onReceive(recvEvent);
}

void loop() { // TODO
  /*sendBytes(1, 32);
  sendBytes(2, 16);
  //_println("H");
  delay(1000);

  sendBytes(1, 33);
  sendBytes(2, 17);
  //_println("i");*/
  delay(1);
}

void reqEvent()
{
  sendBytes(1, 34);
  sendBytes(2, 19);
}

void recvEvent(int numBytes)
{
  _println("Got Recv???");
}
