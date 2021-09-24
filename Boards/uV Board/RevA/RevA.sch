EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 4
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
L Connector_Generic:Conn_02x12_Counter_Clockwise J?
U 1 1 614D23CF
P 4850 1900
F 0 "J?" H 4900 2617 50  0000 C CNN
F 1 "Right Connector" H 4900 2526 50  0000 C CNN
F 2 "" H 4850 1900 50  0001 C CNN
F 3 "~" H 4850 1900 50  0001 C CNN
	1    4850 1900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR?
U 1 1 614DBB26
P 5350 1400
F 0 "#PWR?" H 5350 1250 50  0001 C CNN
F 1 "VCC" H 5365 1573 50  0000 C CNN
F 2 "" H 5350 1400 50  0001 C CNN
F 3 "" H 5350 1400 50  0001 C CNN
	1    5350 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 1400 5150 1400
Wire Wire Line
	5350 1400 5350 1500
Wire Wire Line
	5350 1500 5150 1500
Connection ~ 5350 1400
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
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 614D9C1F
P 3350 1950
F 0 "J?" H 3400 2567 50  0000 C CNN
F 1 "Left Connector" H 3400 2476 50  0000 C CNN
F 2 "" H 3350 1950 50  0001 C CNN
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
$Comp
L power:GNDREF #PWR?
U 1 1 614F8C33
P 3650 800
F 0 "#PWR?" H 3650 550 50  0001 C CNN
F 1 "GNDREF" H 3655 627 50  0000 C CNN
F 2 "" H 3650 800 50  0001 C CNN
F 3 "" H 3650 800 50  0001 C CNN
	1    3650 800 
	1    0    0    -1  
$EndComp
Text Label 3650 650  2    50   ~ 0
GND
Wire Wire Line
	3650 650  3650 800 
$Comp
L power:+3.3V #PWR?
U 1 1 614FB62C
P 4550 750
F 0 "#PWR?" H 4550 600 50  0001 C CNN
F 1 "+3.3V" H 4565 923 50  0000 C CNN
F 2 "" H 4550 750 50  0001 C CNN
F 3 "" H 4550 750 50  0001 C CNN
	1    4550 750 
	1    0    0    -1  
$EndComp
Text Label 4550 950  2    50   ~ 0
3.3V
Wire Wire Line
	4550 950  4550 750 
$Comp
L power:+5V #PWR?
U 1 1 614FCDE4
P 4100 750
F 0 "#PWR?" H 4100 600 50  0001 C CNN
F 1 "+5V" H 4115 923 50  0000 C CNN
F 2 "" H 4100 750 50  0001 C CNN
F 3 "" H 4100 750 50  0001 C CNN
	1    4100 750 
	1    0    0    -1  
$EndComp
Text Label 4100 950  2    50   ~ 0
5V
Wire Wire Line
	4100 950  4100 750 
$Sheet
S 5700 2550 2100 1900
U 614FD8C2
F0 "controller" 50
F1 "controller.sch" 50
$EndSheet
$Sheet
S 8000 2550 2200 1900
U 614FDE40
F0 "Strain_1" 50
F1 "StrainGuage.sch" 50
$EndSheet
$Sheet
S 5700 4700 2100 1650
U 614DF1EE
F0 "Thermo_1" 50
F1 "Thermocouple.sch" 50
$EndSheet
Text Notes 4500 2650 0    50   ~ 0
Pins here are n + 20\n
Text Notes 10600 7650 0    79   ~ 0
A
Text Notes 7350 7550 0    118  ~ 0
MicroVolt Board
$EndSCHEMATC
