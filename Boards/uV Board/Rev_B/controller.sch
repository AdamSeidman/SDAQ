EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
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
L Connector:Conn_01x15_Female J3
U 1 1 614FE43E
P 1600 1550
F 0 "J3" H 1628 1576 50  0000 L CNN
F 1 "Arduino Nano L" H 1628 1485 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x15_P2.54mm_Vertical" H 1600 1550 50  0001 C CNN
F 3 "~" H 1600 1550 50  0001 C CNN
	1    1600 1550
	1    0    0    -1  
$EndComp
Text HLabel 2600 950  0    50   Input ~ 0
GND
Text HLabel 2600 850  0    50   Input ~ 0
5V
Text HLabel 1400 1150 0    50   Input ~ 0
GND
Text HLabel 1400 1050 0    50   Input ~ 0
Reset
NoConn ~ 1400 850 
NoConn ~ 1400 950 
NoConn ~ 1400 1350
NoConn ~ 1400 1450
NoConn ~ 1400 1550
NoConn ~ 1400 1650
NoConn ~ 1400 1750
NoConn ~ 1400 1850
NoConn ~ 1400 1950
NoConn ~ 2600 2150
NoConn ~ 2600 2050
NoConn ~ 2600 1150
NoConn ~ 2600 1050
$Comp
L Connector:Conn_01x15_Female J4
U 1 1 61504D87
P 2800 1550
F 0 "J4" H 3150 2000 50  0000 L CNN
F 1 "Arduino Nano R" H 2950 1900 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x15_P2.54mm_Vertical" H 2800 1550 50  0001 C CNN
F 3 "~" H 2800 1550 50  0001 C CNN
	1    2800 1550
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x03_Counter_Clockwise J5
U 1 1 61567E78
P 4200 1050
F 0 "J5" H 4250 1367 50  0000 C CNN
F 1 "Extra Pins" H 4250 1276 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 4200 1050 50  0001 C CNN
F 3 "~" H 4200 1050 50  0001 C CNN
	1    4200 1050
	1    0    0    -1  
$EndComp
Text HLabel 4000 950  0    50   Input ~ 0
5V
Text Label 4500 1150 0    50   ~ 0
D11
Text Label 4500 1050 0    50   ~ 0
D12
Text Label 4000 1050 2    50   ~ 0
A7
Text Label 4000 1150 2    50   ~ 0
A6
Text HLabel 4500 950  2    50   Input ~ 0
GND
Text HLabel 2550 1650 0    50   Input ~ 0
Strain_4
Text HLabel 2550 1750 0    50   Input ~ 0
Strain_3
Text HLabel 2550 1850 0    50   Input ~ 0
Strain_2
Text HLabel 2550 1950 0    50   Input ~ 0
Strain_1
NoConn ~ 2600 2250
NoConn ~ 1400 2050
Text Notes 2350 1050 0    50   ~ 0
Reset\n
NoConn ~ 1400 1250
Text HLabel 2600 1450 0    50   BiDi ~ 0
I2C_Clock
Text HLabel 2600 1550 0    50   BiDi ~ 0
I2C_Data
Wire Notes Line
	3500 700  3500 2350
Wire Notes Line
	1100 2350 1100 700 
Text Notes 2850 2300 0    50   ~ 0
D13
Text Notes 2850 2000 0    50   ~ 0
A0
Text Notes 2850 1900 0    50   ~ 0
A1
Text Notes 2850 1800 0    50   ~ 0
A2
Text Notes 2850 1700 0    50   ~ 0
A3
Text Notes 2850 1600 0    50   ~ 0
A4
Text Notes 2850 1500 0    50   ~ 0
A5
Text Notes 2850 1400 0    50   ~ 0
A6
Text Notes 2850 1300 0    50   ~ 0
A7
Text Notes 1650 2300 0    50   ~ 0
D12
Text Notes 1650 1300 0    50   ~ 0
D2
Wire Notes Line
	1100 2350 3500 2350
Wire Notes Line
	1100 700  3500 700 
Text Label 2600 1250 2    50   ~ 0
A7
Text Label 2600 1350 2    50   ~ 0
A6
Text Label 1400 2150 2    50   ~ 0
D11
Text Label 1400 2250 2    50   ~ 0
D12
Text Notes 1650 2200 0    50   ~ 0
D11\n
Wire Wire Line
	2550 1650 2600 1650
Wire Wire Line
	2600 1750 2550 1750
Wire Wire Line
	2600 1850 2550 1850
Wire Wire Line
	2600 1950 2550 1950
$EndSCHEMATC
