#ifndef __SDAQ_H__
#define __SDAQ_H__

#include "Wire.h"

#define RPI_DEVC_CODE (0x70)

#define ADC_BOARD     (0x10)
#define STRAIN_BOARD  (0x20)
#define IMU_BOARD     (0x30)
#define BREADBOARD    (0x40)

#define BAUD_RATE     (9600)

#define INFO_MASK     (0x80)
#define DATA_MASK     (~INFO_MASK)

#define SENSOR_ID_POS (1)

// ms delay between transfers
#define DATA_RATE     (40)

void connectDevice(byte MASTER_DEVICE_CODE, byte BOARD_TYPE_ID, byte BOARD_NUM);
void sendBytes(byte SENSOR_ID, byte DATA);

void serialBegin(boolean OUTPUT_ENABLED);
void _println(String s);
void _print(String s);

#endif
