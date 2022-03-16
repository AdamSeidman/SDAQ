EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 13
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 1300 1500 900  600 
U 62325A7E
F0 "sheet62325A7C" 50
F1 "Input.sch" 50
F2 "5V" I L 1300 1600 50 
F3 "GND" I L 1300 1750 50 
F4 "Analog" I L 1300 1900 50 
$EndSheet
$Sheet
S 2650 1500 900  600 
U 6232E183
F0 "sheet6232E17E" 50
F1 "Input.sch" 50
F2 "5V" I L 2650 1600 50 
F3 "GND" I L 2650 1750 50 
F4 "Analog" I L 2650 1900 50 
$EndSheet
$Sheet
S 3950 1500 900  600 
U 6232E335
F0 "sheet6232E330" 50
F1 "Input.sch" 50
F2 "5V" I L 3950 1600 50 
F3 "GND" I L 3950 1750 50 
F4 "Analog" I L 3950 1900 50 
$EndSheet
$Sheet
S 5250 1500 900  600 
U 6232E4F3
F0 "sheet6232E4EE" 50
F1 "Input.sch" 50
F2 "5V" I L 5250 1600 50 
F3 "GND" I L 5250 1750 50 
F4 "Analog" I L 5250 1900 50 
$EndSheet
$Sheet
S 1300 2650 900  600 
U 6232EF2C
F0 "sheet6232EF24" 50
F1 "Input.sch" 50
F2 "5V" I L 1300 2750 50 
F3 "GND" I L 1300 2900 50 
F4 "Analog" I L 1300 3050 50 
$EndSheet
$Sheet
S 2650 2650 900  600 
U 6232EF31
F0 "sheet6232EF25" 50
F1 "Input.sch" 50
F2 "5V" I L 2650 2750 50 
F3 "GND" I L 2650 2900 50 
F4 "Analog" I L 2650 3050 50 
$EndSheet
$Sheet
S 3950 2650 900  600 
U 6232EF36
F0 "sheet6232EF26" 50
F1 "Input.sch" 50
F2 "5V" I L 3950 2750 50 
F3 "GND" I L 3950 2900 50 
F4 "Analog" I L 3950 3050 50 
$EndSheet
$Sheet
S 5250 2650 900  600 
U 6232EF3B
F0 "sheet6232EF27" 50
F1 "Input.sch" 50
F2 "5V" I L 5250 2750 50 
F3 "GND" I L 5250 2900 50 
F4 "Analog" I L 5250 3050 50 
$EndSheet
Text Label 1300 1600 2    50   ~ 0
5V
Text Label 1300 1750 2    50   ~ 0
GND
Text Label 2650 1600 2    50   ~ 0
5V
Text Label 2650 1750 2    50   ~ 0
GND
Text Label 3950 1600 2    50   ~ 0
5V
Text Label 3950 1750 2    50   ~ 0
GND
Text Label 5250 1600 2    50   ~ 0
5V
Text Label 5250 1750 2    50   ~ 0
GND
Text Label 5250 2750 2    50   ~ 0
5V
Text Label 5250 2900 2    50   ~ 0
GND
Text Label 3950 2750 2    50   ~ 0
5V
Text Label 3950 2900 2    50   ~ 0
GND
Text Label 2650 2750 2    50   ~ 0
5V
Text Label 2650 2900 2    50   ~ 0
GND
Text Label 1300 2750 2    50   ~ 0
5V
Text Label 1300 2900 2    50   ~ 0
GND
Text Label 2600 1000 2    50   ~ 0
5V
Text Label 2600 1150 2    50   ~ 0
GND
Text HLabel 2900 1000 2    50   Input ~ 0
5V
Text HLabel 2900 1150 2    50   Input ~ 0
GND
Wire Wire Line
	2900 1000 2600 1000
Wire Wire Line
	2600 1150 2900 1150
Text HLabel 1300 1900 0    50   Input ~ 0
A0
Text HLabel 5250 3050 0    50   Input ~ 0
A7
Text HLabel 2650 1900 0    50   Input ~ 0
A1
Text HLabel 5250 1900 0    50   Input ~ 0
A3
Text HLabel 1300 3050 0    50   Input ~ 0
A4
Text HLabel 2650 3050 0    50   Input ~ 0
A5
Text HLabel 3950 3050 0    50   Input ~ 0
A6
$Comp
L Connector:Screw_Terminal_01x04 J6
U 1 1 62338C0C
P 2450 3900
F 0 "J6" H 2530 3892 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 2530 3801 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 2450 3900 50  0001 C CNN
F 3 "~" H 2450 3900 50  0001 C CNN
	1    2450 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J8
U 1 1 62339E59
P 2450 4800
F 0 "J8" H 2530 4792 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 2530 4701 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 2450 4800 50  0001 C CNN
F 3 "~" H 2450 4800 50  0001 C CNN
	1    2450 4800
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J7
U 1 1 6233ABB7
P 2450 4350
F 0 "J7" H 2530 4342 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 2530 4251 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 2450 4350 50  0001 C CNN
F 3 "~" H 2450 4350 50  0001 C CNN
	1    2450 4350
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J9
U 1 1 6234244F
P 4050 3850
F 0 "J9" H 4130 3842 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 4130 3751 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 4050 3850 50  0001 C CNN
F 3 "~" H 4050 3850 50  0001 C CNN
	1    4050 3850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J11
U 1 1 62342455
P 4050 4750
F 0 "J11" H 4130 4742 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 4130 4651 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 4050 4750 50  0001 C CNN
F 3 "~" H 4050 4750 50  0001 C CNN
	1    4050 4750
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J10
U 1 1 6234245B
P 4050 4300
F 0 "J10" H 4130 4292 50  0000 L CNN
F 1 "Screw_Terminal_01x04" H 4130 4201 50  0000 L CNN
F 2 "Spring_Terminal_4Pin:1984989" H 4050 4300 50  0001 C CNN
F 3 "~" H 4050 4300 50  0001 C CNN
	1    4050 4300
	1    0    0    -1  
$EndComp
Text Label 2250 3800 2    50   ~ 0
5V
Text Label 2250 4100 2    50   ~ 0
5V
Text Label 2250 4450 2    50   ~ 0
5V
Text Label 2250 4800 2    50   ~ 0
5V
Text Label 3850 3750 2    50   ~ 0
5V
Text Label 3850 4050 2    50   ~ 0
5V
Text Label 3850 4400 2    50   ~ 0
5V
Text Label 3850 4750 2    50   ~ 0
5V
Text Label 2250 4000 2    50   ~ 0
GND
Text Label 2250 4350 2    50   ~ 0
GND
Text Label 2250 4700 2    50   ~ 0
GND
Text Label 2250 5000 2    50   ~ 0
GND
Text Label 3850 3950 2    50   ~ 0
GND
Text Label 3850 4300 2    50   ~ 0
GND
Text Label 3850 4650 2    50   ~ 0
GND
Text Label 3850 4950 2    50   ~ 0
GND
Text HLabel 2250 3900 0    50   Input ~ 0
A0
Text HLabel 2250 4250 0    50   Input ~ 0
A1
Text HLabel 3950 1900 0    50   Input ~ 0
A2
Text HLabel 2250 4550 0    50   Input ~ 0
A2
Text HLabel 2250 4900 0    50   Input ~ 0
A3
Text HLabel 3850 3850 0    50   Input ~ 0
A4
Text HLabel 3850 4200 0    50   Input ~ 0
A5
Text HLabel 3850 4500 0    50   Input ~ 0
A6
Text HLabel 3850 4850 0    50   Input ~ 0
A7
$Comp
L Connector_Generic:Conn_02x05_Top_Bottom J12
U 1 1 623441A1
P 5950 4250
F 0 "J12" H 6000 4667 50  0000 C CNN
F 1 "Conn_02x05_Top_Bottom" H 6000 4576 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical" H 5950 4250 50  0001 C CNN
F 3 "~" H 5950 4250 50  0001 C CNN
	1    5950 4250
	1    0    0    -1  
$EndComp
Text Label 5750 4050 2    50   ~ 0
5V
Text Label 6250 4450 0    50   ~ 0
GND
Text HLabel 5750 4150 0    50   Input ~ 0
A0
Text HLabel 5750 4250 0    50   Input ~ 0
A1
Text HLabel 5750 4350 0    50   Input ~ 0
A2
Text HLabel 5750 4450 0    50   Input ~ 0
A3
Text HLabel 6250 4050 2    50   Input ~ 0
A4
Text HLabel 6250 4150 2    50   Input ~ 0
A5
Text HLabel 6250 4250 2    50   Input ~ 0
A6
Text HLabel 6250 4350 2    50   Input ~ 0
A7
$EndSCHEMATC
