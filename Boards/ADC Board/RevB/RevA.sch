EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 13
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
L Connector_Generic:Conn_02x10_Counter_Clockwise J1
U 1 1 615E5E26
P 1600 1850
F 0 "J1" H 1650 2467 50  0000 C CNN
F 1 "Left Connector" H 1650 2376 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 1600 1850 50  0001 C CNN
F 3 "~" H 1600 1850 50  0001 C CNN
	1    1600 1850
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x12_Counter_Clockwise J2
U 1 1 615E7214
P 3000 1850
F 0 "J2" H 3050 2567 50  0000 C CNN
F 1 "Right Connector" H 3050 2476 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 3000 1850 50  0001 C CNN
F 3 "~" H 3000 1850 50  0001 C CNN
	1    3000 1850
	1    0    0    -1  
$EndComp
Text Label 1400 1450 2    50   ~ 0
3.3V
Text Label 1400 1950 2    50   ~ 0
GND
Text Label 1400 2250 2    50   ~ 0
GND
Text Label 1900 1450 0    50   ~ 0
GND
Text Label 1900 2050 0    50   ~ 0
GND
Text Label 1900 1750 0    50   ~ 0
3.3V
Text Label 2800 1750 2    50   ~ 0
GND
Text Label 2800 2250 2    50   ~ 0
GND
Text Label 3300 2350 0    50   ~ 0
GND
Text Label 3300 1850 0    50   ~ 0
GND
Wire Wire Line
	3300 1350 3550 1350
Wire Wire Line
	3550 1350 3550 1400
Wire Wire Line
	3550 1450 3300 1450
Text Notes 2650 2600 0    50   ~ 0
Pins here are n + 20
Text Label 4200 1050 0    50   ~ 0
Reset
Text Label 1400 1650 2    50   ~ 0
I2C_Data
Text Label 1400 1850 2    50   ~ 0
I2C_Clock
$Comp
L Mechanical:MountingHole M2.5
U 1 1 616626E5
P 3950 3550
F 0 "M2.5" H 4050 3596 50  0000 L CNN
F 1 "CMH" H 4050 3505 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 3950 3550 50  0001 C CNN
F 3 "~" H 3950 3550 50  0001 C CNN
	1    3950 3550
	1    0    0    -1  
$EndComp
$Sheet
S 4500 4050 1350 900 
U 61663709
F0 "5v_regulator" 50
F1 "5v_regulator.sch" 50
F2 "Vcc" I L 4500 4200 50 
F3 "GND" I L 4500 4350 50 
F4 "5V" I L 4500 4500 50 
$EndSheet
Text Label 4500 4200 2    50   ~ 0
VCC
Text Label 3400 4500 2    50   ~ 0
5V
Text Label 4500 4350 2    50   ~ 0
GND
Text Label 3650 1400 0    50   ~ 0
VCC
NoConn ~ 1900 1550
NoConn ~ 1900 1650
NoConn ~ 1900 1850
NoConn ~ 1900 1950
NoConn ~ 1400 2050
NoConn ~ 1400 2150
NoConn ~ 1400 2350
NoConn ~ 1900 2350
NoConn ~ 1900 2250
NoConn ~ 1900 2150
NoConn ~ 2800 2450
NoConn ~ 2800 2350
NoConn ~ 2800 2150
NoConn ~ 2800 2050
NoConn ~ 2800 1950
NoConn ~ 2800 1850
NoConn ~ 2800 1650
NoConn ~ 2800 1550
NoConn ~ 2800 1450
NoConn ~ 2800 1350
NoConn ~ 3300 1750
NoConn ~ 3300 1950
NoConn ~ 3300 2050
NoConn ~ 3300 2150
NoConn ~ 3300 2250
NoConn ~ 3300 2450
Wire Wire Line
	3650 1400 3550 1400
Connection ~ 3550 1400
Wire Wire Line
	3550 1400 3550 1450
Text Label 3300 1650 0    50   ~ 0
Interconnect
Text Label 3100 2900 2    50   ~ 0
Interconnect
Wire Wire Line
	3100 2900 3200 2900
NoConn ~ 3200 2900
NoConn ~ 1400 1550
NoConn ~ 1400 1750
Text Notes 1350 1550 2    50   ~ 0
5V
Text Notes 1350 1750 2    50   ~ 0
5V
$Sheet
S 5550 2400 750  700 
U 62315BFE
F0 "BoardID" 50
F1 "BoardID.sch" 50
F2 "5V" I L 5550 2500 50 
F3 "ID0" I R 6300 2500 50 
F4 "ID1" I R 6300 2600 50 
F5 "ID2" I R 6300 2700 50 
F6 "ID3" I R 6300 2800 50 
F7 "GND" I L 5550 2600 50 
$EndSheet
Text Label 5550 2600 2    50   ~ 0
GND
Text Label 5550 2500 2    50   ~ 0
5V
$Comp
L Switch:SW_DIP_x01 SW1
U 1 1 62322B6A
P 3900 4500
F 0 "SW1" H 3900 4767 50  0000 C CNN
F 1 "SW_DIP_x01" H 3900 4676 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_DIP_SPSTx01_Slide_9.78x4.72mm_W8.61mm_P2.54mm" H 3900 4500 50  0001 C CNN
F 3 "~" H 3900 4500 50  0001 C CNN
	1    3900 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 4500 4500 4500
$Sheet
S 5100 5550 1250 1650
U 62325883
F0 "Analog" 50
F1 "Analog.sch" 50
F2 "5V" I L 5100 5800 50 
F3 "GND" I L 5100 6050 50 
F4 "A0" I R 6350 5800 50 
F5 "A7" I R 6350 6850 50 
F6 "A1" I R 6350 5950 50 
F7 "A2" I R 6350 6100 50 
F8 "A3" I R 6350 6250 50 
F9 "A4" I R 6350 6400 50 
F10 "A5" I R 6350 6550 50 
F11 "A6" I R 6350 6700 50 
$EndSheet
Text Label 5100 5800 2    50   ~ 0
5V
Text Label 5100 6050 2    50   ~ 0
GND
Text Label 6350 5800 0    50   ~ 0
A0
Text Label 6350 5950 0    50   ~ 0
A1
Text Label 6350 6100 0    50   ~ 0
A2
Text Label 6350 6400 0    50   ~ 0
A4
Text Label 6350 6250 0    50   ~ 0
A3
Text Label 6350 6550 0    50   ~ 0
A5
Text Label 6350 6700 0    50   ~ 0
A6
Text Label 6350 6850 0    50   ~ 0
A7
$Comp
L Simulation_SPICE:DIODE D3
U 1 1 6232B450
P 4050 1050
F 0 "D3" H 4050 1267 50  0000 C CNN
F 1 "DIODE" H 4050 1176 50  0000 C CNN
F 2 "Diode_SMD:D_SMA" H 4050 1050 50  0001 C CNN
F 3 "~" H 4050 1050 50  0001 C CNN
F 4 "Y" H 4050 1050 50  0001 L CNN "Spice_Netlist_Enabled"
F 5 "D" H 4050 1050 50  0001 L CNN "Spice_Primitive"
	1    4050 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 1550 3900 1550
Wire Wire Line
	3900 1550 3900 1050
$Sheet
S 7250 900  3200 2500
U 62331E1A
F0 "Arduino" 50
F1 "controller.sch" 50
F2 "GND" I L 7250 1600 50 
F3 "Reset" I L 7250 2150 50 
F4 "5V" I L 7250 1450 50 
F5 "A0" I R 10450 1350 50 
F6 "A1" I R 10450 1550 50 
F7 "A2" I R 10450 1750 50 
F8 "A3" I R 10450 1950 50 
F9 "A4" I R 10450 2150 50 
F10 "A5" I R 10450 2350 50 
F11 "A6" I R 10450 2550 50 
F12 "A7" I R 10450 2750 50 
F13 "D0" I L 7250 2500 50 
F14 "D1" I L 7250 2700 50 
F15 "D2" I L 7250 2900 50 
F16 "D3" I L 7250 3100 50 
F17 "I2C_Clock" B L 7250 1050 50 
F18 "I2C_Data" B L 7250 1200 50 
$EndSheet
Text Label 7250 1600 2    50   ~ 0
GND
Text Label 7250 1450 2    50   ~ 0
5V
Text Label 10450 1350 0    50   ~ 0
A0
Text Label 10450 1550 0    50   ~ 0
A1
Text Label 10450 1750 0    50   ~ 0
A2
Text Label 10450 2150 0    50   ~ 0
A4
Text Label 10450 1950 0    50   ~ 0
A3
Text Label 10450 2350 0    50   ~ 0
A5
Text Label 10450 2550 0    50   ~ 0
A6
Text Label 10450 2750 0    50   ~ 0
A7
Text Label 7250 1200 2    50   ~ 0
I2C_Data
Text Label 7250 1050 2    50   ~ 0
I2C_Clock
Text Label 7250 2150 2    50   ~ 0
Reset
Wire Wire Line
	6300 2500 7250 2500
Wire Wire Line
	6300 2600 7200 2600
Wire Wire Line
	7200 2600 7200 2700
Wire Wire Line
	7200 2700 7250 2700
Wire Wire Line
	6300 2700 7150 2700
Wire Wire Line
	7150 2700 7150 2900
Wire Wire Line
	7150 2900 7250 2900
Wire Wire Line
	6300 2800 7100 2800
Wire Wire Line
	7100 2800 7100 3100
Wire Wire Line
	7100 3100 7250 3100
Text Label 3400 4800 2    50   ~ 0
GND
$Comp
L Device:LED D2
U 1 1 6233EF46
P 3600 4650
F 0 "D2" V 3639 4532 50  0000 R CNN
F 1 "LED" V 3548 4532 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric" H 3600 4650 50  0001 C CNN
F 3 "~" H 3600 4650 50  0001 C CNN
	1    3600 4650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3400 4500 3600 4500
Connection ~ 3600 4500
Wire Wire Line
	3400 4800 3600 4800
$EndSCHEMATC
