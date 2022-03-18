EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 13 13
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CSTCE16M0V53-R0:CSTCE16M0V53-R0 Y1
U 1 1 6234D0B2
P 1600 4450
F 0 "Y1" H 1600 4817 50  0000 C CNN
F 1 "CSTCE16M0V53-R0" H 1600 4726 50  0000 C CNN
F 2 "CSTCE16M0V53-R0:OSC_CSTCE16M0V53-R0" H 1600 4450 50  0001 L BNN
F 3 "1.0 mm" H 1600 4450 50  0001 L BNN
F 4 "Murata Electronics" H 1600 4450 50  0001 L BNN "Field4"
F 5 "Manufacturer Recommendations" H 1600 4450 50  0001 L BNN "Field5"
F 6 "04.8.24" H 1600 4450 50  0001 L BNN "Field6"
	1    1600 4450
	0    1    1    0   
$EndComp
Wire Wire Line
	2100 4350 2100 3950
Wire Wire Line
	1700 4950 2100 4950
Wire Wire Line
	2100 4950 2100 4450
Wire Wire Line
	1700 3950 2100 3950
Text HLabel 1200 4450 0    50   Input ~ 0
GND
Wire Wire Line
	8500 4850 9100 4850
Wire Wire Line
	9100 4850 9100 4900
Wire Wire Line
	9100 4900 9250 4900
$Comp
L Device:C C5
U 1 1 6235B1D1
P 8650 4950
F 0 "C5" V 8398 4950 50  0000 C CNN
F 1 "100nF" V 8489 4950 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8688 4800 50  0001 C CNN
F 3 "~" H 8650 4950 50  0001 C CNN
	1    8650 4950
	0    1    1    0   
$EndComp
Wire Wire Line
	9100 4900 9100 4950
Wire Wire Line
	9100 4950 8800 4950
Connection ~ 9100 4900
Text HLabel 9250 4900 2    50   Input ~ 0
GND
Text HLabel 8500 4050 2    50   Input ~ 0
Reset
Text HLabel 8500 5150 2    50   Input ~ 0
5V
Text HLabel 2400 4100 0    50   Input ~ 0
5V
Wire Wire Line
	2900 4250 2750 4250
Wire Wire Line
	2750 4250 2750 4100
Wire Wire Line
	2750 4050 2900 4050
Wire Wire Line
	2400 4100 2750 4100
Connection ~ 2750 4100
Wire Wire Line
	2750 4100 2750 4050
Wire Wire Line
	2900 4150 2850 4150
Wire Wire Line
	2850 4150 2850 3950
Wire Wire Line
	2850 3950 2900 3950
Text HLabel 2400 3950 0    50   Input ~ 0
GND
Wire Wire Line
	2850 3950 2400 3950
Connection ~ 2850 3950
Text HLabel 5800 5700 0    50   Input ~ 0
GND
Wire Wire Line
	5800 5550 5800 5700
Wire Wire Line
	2100 4350 2900 4350
Wire Wire Line
	2100 4450 2900 4450
NoConn ~ 2900 3850
NoConn ~ 2900 4950
NoConn ~ 2900 5050
$Comp
L 2020-11-11_15-40-12:ATMEGA328P-MUR U1
U 1 1 6234A28C
P 2900 3750
F 0 "U1" H 5700 4137 60  0000 C CNN
F 1 "ATMEGA328P-MUR" H 5700 4031 60  0000 C CNN
F 2 "ATMEGA_Import:ATMEGA328P-MUR" H 5700 3990 60  0001 C CNN
F 3 "" H 2900 3750 60  0000 C CNN
	1    2900 3750
	1    0    0    -1  
$EndComp
Text HLabel 8500 4650 2    50   Input ~ 0
A0
Text HLabel 8500 4550 2    50   Input ~ 0
A1
Text HLabel 8500 4450 2    50   Input ~ 0
A2
Text HLabel 8500 4350 2    50   Input ~ 0
A3
Text HLabel 8500 5050 2    50   Input ~ 0
A4
Text HLabel 8500 4750 2    50   Input ~ 0
A5
Text HLabel 2900 4650 0    50   Input ~ 0
A6
Text HLabel 2900 4750 0    50   Input ~ 0
A7
Text HLabel 8500 3950 2    50   Input ~ 0
D0
Text HLabel 8500 3850 2    50   Input ~ 0
D1
Text HLabel 8500 3750 2    50   Input ~ 0
D2
Text HLabel 2900 3750 0    50   Input ~ 0
D3
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J21
U 1 1 62316B37
P 1500 5900
F 0 "J21" H 1550 6217 50  0000 C CNN
F 1 "Conn_02x03_Odd_Even" H 1550 6126 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 1500 5900 50  0001 C CNN
F 3 "~" H 1500 5900 50  0001 C CNN
	1    1500 5900
	1    0    0    -1  
$EndComp
Text HLabel 1800 6000 2    50   Input ~ 0
GND
Text HLabel 1800 5800 2    50   Input ~ 0
5V
Text HLabel 1300 6000 0    50   Input ~ 0
Reset
Text HLabel 8500 4150 2    50   BiDi ~ 0
I2C_Clock
Text HLabel 8500 4250 2    50   BiDi ~ 0
I2C_Data
NoConn ~ 2900 4850
NoConn ~ 2900 4550
Text Notes 8950 4300 0    50   ~ 0
A4\n
Text Notes 8950 4150 0    50   ~ 0
A5
Text Notes 2600 4750 0    50   ~ 0
D#\n
Text Label 2900 5150 2    50   ~ 0
MOSI
Text Label 2900 5250 2    50   ~ 0
MISO
Text Label 8500 5250 0    50   ~ 0
SCK
Text Label 1300 5800 2    50   ~ 0
MISO
Text Label 1300 5900 2    50   ~ 0
SCK
Text Label 1800 5900 0    50   ~ 0
MOSI
$EndSCHEMATC
