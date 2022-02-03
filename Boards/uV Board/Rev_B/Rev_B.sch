EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 7
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
L Connector_Generic:Conn_02x12_Counter_Clockwise J2
U 1 1 614D23CF
P 4850 1900
F 0 "J2" H 4900 2617 50  0000 C CNN
F 1 "Right Connector" H 4900 2526 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 4850 1900 50  0001 C CNN
F 3 "~" H 4850 1900 50  0001 C CNN
	1    4850 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 1400 5150 1400
Wire Wire Line
	5350 1400 5350 1500
Wire Wire Line
	5350 1500 5150 1500
Text Label 5150 2400 0    50   ~ 0
GND
Text Label 4650 1800 2    50   ~ 0
GND
Text Label 4650 2300 2    50   ~ 0
GND
Text Label 3150 2050 2    50   ~ 0
GND
Text Label 3650 2150 0    50   ~ 0
GND
Text Label 3150 2350 2    50   ~ 0
GND
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J1
U 1 1 614D9C1F
P 3350 1950
F 0 "J1" H 3400 2567 50  0000 C CNN
F 1 "Left Connector" H 3400 2476 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 3350 1950 50  0001 C CNN
F 3 "~" H 3350 1950 50  0001 C CNN
	1    3350 1950
	1    0    0    -1  
$EndComp
Text Label 3650 1550 0    50   ~ 0
GND
Text Label 5150 1900 0    50   ~ 0
GND
Text Label 3650 1850 0    50   ~ 0
3.3V
Text Label 3150 1850 2    50   ~ 0
5V
Text Label 3150 1650 2    50   ~ 0
5V
Text Label 3150 1550 2    50   ~ 0
3.3V
$Sheet
S 5750 2550 2100 1900
U 614FD8C2
F0 "controller" 50
F1 "controller.sch" 50
F2 "GND" I R 7850 2800 50 
F3 "5V" I R 7850 2650 50 
F4 "Reset" I L 5750 3000 50 
F5 "Strain_3" I R 7850 3750 50 
F6 "Strain_2" I R 7850 3900 50 
F7 "Strain_1" I R 7850 4050 50 
F8 "I2C_Clock" B L 5750 3350 50 
F9 "I2C_Data" B L 5750 3500 50 
$EndSheet
Text Notes 4500 2650 0    50   ~ 0
Pins here are n + 20\n
Text Notes 10600 7650 0    79   ~ 0
A
Text Notes 7350 7550 0    118  ~ 0
MicroVolt Board
$Sheet
S 9450 2550 800  700 
U 6153C564
F0 "Strain_2" 50
F1 "StrainGuage.sch" 50
F2 "5V" I R 10250 2700 50 
F3 "GND" I R 10250 2800 50 
F4 "Strain_Out" I R 10250 2900 50 
$EndSheet
$Sheet
S 8500 3550 800  700 
U 61575900
F0 "Strain_3" 50
F1 "StrainGuage.sch" 50
F2 "5V" I L 8500 3700 50 
F3 "GND" I L 8500 3800 50 
F4 "Strain_Out" I L 8500 3900 50 
$EndSheet
Wire Wire Line
	10250 2700 10400 2700
Wire Wire Line
	10400 2700 10400 3450
Text Label 8000 2450 0    50   ~ 0
5V
Text Label 8250 2500 0    50   ~ 0
GND
Wire Wire Line
	10300 2800 10250 2800
Text Label 7850 3900 0    50   ~ 0
Strain_2
Text Label 10600 2900 0    50   ~ 0
Strain_2
Wire Wire Line
	10250 2900 10600 2900
Text Label 5150 1600 0    50   ~ 0
Reset
Text Label 5750 3000 2    50   ~ 0
Reset
$Sheet
S 8500 2550 800  700 
U 614FDE40
F0 "Strain_1" 50
F1 "StrainGuage.sch" 50
F2 "5V" I L 8500 2650 50 
F3 "GND" I L 8500 2800 50 
F4 "Strain_Out" I L 8500 2900 50 
$EndSheet
Text Label 10700 3200 0    50   ~ 0
GND
Text Label 10700 3450 0    50   ~ 0
5V
Wire Wire Line
	10700 3200 10300 3200
Wire Wire Line
	10300 3200 10300 2800
Wire Wire Line
	10700 3450 10400 3450
Text Label 3150 1950 2    50   ~ 0
I2C_Clock
Text Label 3150 1750 2    50   ~ 0
I2C_Data
Text Label 5750 3350 2    50   ~ 0
I2C_Clock
Text Label 5750 3500 2    50   ~ 0
I2C_Data
Text Label 5150 1700 0    50   ~ 0
Interconnect
$Sheet
S 3600 3550 1050 900 
U 616005C4
F0 "5v_regulator" 50
F1 "5v_regulator.sch" 50
F2 "Vcc" I L 3600 3750 50 
F3 "GND" I L 3600 3900 50 
F4 "5V" I L 3600 4050 50 
$EndSheet
Text Label 5350 1400 0    50   ~ 0
VCC
Text Label 3600 3750 2    50   ~ 0
VCC
Text Label 3600 4050 2    50   ~ 0
5V
Text Label 3600 3900 2    50   ~ 0
GND
NoConn ~ 3150 2150
NoConn ~ 3150 2250
NoConn ~ 3150 2450
NoConn ~ 3650 2450
NoConn ~ 3650 2350
NoConn ~ 3650 2250
NoConn ~ 3650 2050
NoConn ~ 3650 1950
NoConn ~ 3650 1750
NoConn ~ 3650 1650
NoConn ~ 4650 1400
NoConn ~ 4650 1500
NoConn ~ 4650 1600
NoConn ~ 4650 1700
NoConn ~ 4650 1900
NoConn ~ 4650 2000
NoConn ~ 4650 2100
NoConn ~ 4650 2200
NoConn ~ 4650 2400
NoConn ~ 4650 2500
NoConn ~ 5150 2500
NoConn ~ 5150 2300
NoConn ~ 5150 2200
NoConn ~ 5150 2100
NoConn ~ 5150 2000
NoConn ~ 5150 1800
NoConn ~ 5150 1700
Wire Wire Line
	8500 3800 8450 3800
Wire Wire Line
	8450 3800 8450 2800
Wire Wire Line
	8450 2800 8500 2800
Wire Wire Line
	8500 3700 8350 3700
Wire Wire Line
	8350 3700 8350 2650
Wire Wire Line
	8350 2650 8500 2650
Wire Wire Line
	7850 2650 8000 2650
Connection ~ 8350 2650
Wire Wire Line
	7850 2800 8250 2800
Connection ~ 8450 2800
Wire Wire Line
	8250 2500 8250 2800
Connection ~ 8250 2800
Wire Wire Line
	8250 2800 8450 2800
Wire Wire Line
	8000 2450 8000 2650
Connection ~ 8000 2650
Wire Wire Line
	8000 2650 8350 2650
Text Label 8350 4300 2    50   ~ 0
Strain_3
Text Label 7850 3750 0    50   ~ 0
Strain_3
Text Label 8250 2900 2    50   ~ 0
Strain_1
Text Label 7850 4050 0    50   ~ 0
Strain_1
Wire Wire Line
	8500 2900 8250 2900
Wire Wire Line
	8500 3900 8350 3900
Wire Wire Line
	8350 3900 8350 4300
NoConn ~ 6350 1600
$Sheet
S 1850 3550 1200 900 
U 61F58F90
F0 "Holes" 50
F1 "Holes.sch" 50
$EndSheet
$EndSCHEMATC
