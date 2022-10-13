#ifndef __SDAQ_H__
#define __SDAQ_H__

#include "Wire.h"
#include <stdint.h>
#define ADC_BOARD     (0x08)
#define STRAIN_BOARD  (0x10)
#define IMU_BOARD     (0x18)

#define OTHER_1       (0x20)
#define OTHER_2       (0x28)
#define OTHER_3       (0x30)
#define OTHER_4       (0x38)
#define OTHER_5       (0x40)
#define OTHER_6       (0x48)
#define OTHER_7       (0x50)
#define OTHER_8       (0x58)
#define OTHER_9       (0x60)
#define OTHER_10      (0x68)
#define OTHER_11      (0x70)

#define BAUD_RATE     (9600)
#define I2C_RATE      (1000000)

void connectDevice(byte BOARD_TYPE_ID, byte BOARD_NUM);
void serialBegin(boolean OUTPUT_ENABLED);
void _println(String s);
void _print(String s);

void setupBoard();
void requestEvent();

#endif
