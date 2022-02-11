EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 2
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
L Device:R R2
U 1 1 61FB05A5
P 8350 1625
F 0 "R2" H 8420 1671 50  0000 L CNN
F 1 "3.6k" H 8420 1580 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8280 1625 50  0001 C CNN
F 3 "~" H 8350 1625 50  0001 C CNN
	1    8350 1625
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 61FB0715
P 8375 3450
F 0 "R3" H 8445 3496 50  0000 L CNN
F 1 "10k" H 8445 3405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8305 3450 50  0001 C CNN
F 3 "~" H 8375 3450 50  0001 C CNN
	1    8375 3450
	-1   0    0    1   
$EndComp
$Comp
L Device:R R4
U 1 1 61FB095E
P 9050 2300
F 0 "R4" H 9120 2346 50  0000 L CNN
F 1 "47k" H 9120 2255 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8980 2300 50  0001 C CNN
F 3 "~" H 9050 2300 50  0001 C CNN
	1    9050 2300
	0    1    1    0   
$EndComp
$Comp
L Device:R R6
U 1 1 61FB0E2F
P 5800 2150
F 0 "R6" H 5870 2196 50  0000 L CNN
F 1 "22k" H 5870 2105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5730 2150 50  0001 C CNN
F 3 "~" H 5800 2150 50  0001 C CNN
	1    5800 2150
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 61FB1050
P 6250 2150
F 0 "R7" H 6320 2196 50  0000 L CNN
F 1 "470k" H 6320 2105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6180 2150 50  0001 C CNN
F 3 "~" H 6250 2150 50  0001 C CNN
	1    6250 2150
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R8
U 1 1 61FB11E3
P 6850 2350
F 0 "R8" H 6920 2396 50  0000 L CNN
F 1 "3.6k" H 6920 2305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6780 2350 50  0001 C CNN
F 3 "~" H 6850 2350 50  0001 C CNN
	1    6850 2350
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R9
U 1 1 61FB1409
P 5350 2150
F 0 "R9" H 5420 2196 50  0000 L CNN
F 1 "3.6k" H 5420 2105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5280 2150 50  0001 C CNN
F 3 "~" H 5350 2150 50  0001 C CNN
	1    5350 2150
	0    1    1    0   
$EndComp
$Comp
L Device:C C6
U 1 1 61FB4122
P 8375 3750
F 0 "C6" H 8490 3796 50  0000 L CNN
F 1 "100nF" H 8490 3705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8413 3600 50  0001 C CNN
F 3 "~" H 8375 3750 50  0001 C CNN
	1    8375 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:C C7
U 1 1 61FB4280
P 6850 2000
F 0 "C7" H 6965 2046 50  0000 L CNN
F 1 "100nF" H 6965 1955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6888 1850 50  0001 C CNN
F 3 "~" H 6850 2000 50  0001 C CNN
	1    6850 2000
	0    -1   -1   0   
$EndComp
$Comp
L Device:C C8
U 1 1 61FB43E5
P 9400 2750
F 0 "C8" H 9515 2796 50  0000 L CNN
F 1 "100nF" H 9515 2705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 9438 2600 50  0001 C CNN
F 3 "~" H 9400 2750 50  0001 C CNN
	1    9400 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT RP1
U 1 1 61FBB9DD
P 4250 2150
F 0 "RP1" H 4181 2196 50  0000 R CNN
F 1 "R_POT" H 4181 2105 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3296W_Vertical" H 4250 2150 50  0001 C CNN
F 3 "~" H 4250 2150 50  0001 C CNN
	1    4250 2150
	0    1    1    0   
$EndComp
Text Label 9800 2300 0    50   ~ 0
OUT
$Comp
L Device:C C9
U 1 1 61FB462A
P 8350 1175
F 0 "C9" H 8465 1221 50  0000 L CNN
F 1 "100nF" H 8465 1130 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8388 1025 50  0001 C CNN
F 3 "~" H 8350 1175 50  0001 C CNN
	1    8350 1175
	1    0    0    -1  
$EndComp
Wire Wire Line
	8650 2300 8700 2300
Wire Notes Line
	575  2925 575  1000
$Comp
L Amplifier_Operational:LM358 U1
U 2 1 6204AE85
P 8350 2300
F 0 "U1" H 8350 2667 50  0000 C CNN
F 1 "LM358" H 8350 2576 50  0000 C CNN
F 2 "LM358:SOIC127P599X175-8N" H 8350 2300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2904-n.pdf" H 8350 2300 50  0001 C CNN
	2    8350 2300
	1    0    0    -1  
$EndComp
$Sheet
S 2000 1950 1450 900 
U 61FEE0CC
F0 "Regulator" 50
F1 "Regulator.sch" 50
F2 "GND" I L 2000 2600 50 
F3 "Vcc" I L 2000 2150 50 
F4 "5V" I R 3450 2150 50 
$EndSheet
$Comp
L Connector:Conn_01x03_Male J1
U 1 1 61FEED06
P 1400 2250
F 0 "J1" H 1508 2531 50  0000 C CNN
F 1 "Conn_01x03_Male" H 1508 2440 50  0000 C CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x03_P1.00mm_Vertical" H 1400 2250 50  0001 C CNN
F 3 "~" H 1400 2250 50  0001 C CNN
	1    1400 2250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J2
U 1 1 61FEFF1D
P 5000 1950
F 0 "J2" H 5108 2131 50  0000 C CNN
F 1 "Conn_01x02_Male" H 5108 2040 50  0000 C CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 5000 1950 50  0001 C CNN
F 3 "~" H 5000 1950 50  0001 C CNN
	1    5000 1950
	0    1    1    0   
$EndComp
Wire Wire Line
	1600 2150 2000 2150
Text GLabel 1600 2250 2    50   Input ~ 0
Out
Text GLabel 9850 2300 2    50   Input ~ 0
Out
Connection ~ 8700 2300
Wire Wire Line
	8700 2300 8900 2300
Wire Wire Line
	8350 1325 8350 1475
Wire Wire Line
	5000 2150 5200 2150
$Comp
L Device:C C5
U 1 1 61FB3F31
P 7575 2400
F 0 "C5" H 7690 2446 50  0000 L CNN
F 1 "100nF" H 7690 2355 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 7613 2250 50  0001 C CNN
F 3 "~" H 7575 2400 50  0001 C CNN
	1    7575 2400
	0    1    1    0   
$EndComp
Wire Wire Line
	6700 2350 6550 2350
Wire Wire Line
	6550 2350 6550 2150
Wire Wire Line
	7100 2350 7000 2350
Wire Wire Line
	6700 2000 6550 2000
Wire Wire Line
	7000 2000 7100 2000
Wire Wire Line
	4250 2300 4250 3050
Wire Wire Line
	8700 2300 8700 3100
Wire Wire Line
	3450 2150 4100 2150
Wire Wire Line
	4400 2150 4900 2150
Wire Wire Line
	5500 2150 5650 2150
Wire Wire Line
	6400 2150 6550 2150
Connection ~ 6550 2150
Wire Wire Line
	6550 2150 6550 2000
Wire Wire Line
	5950 2150 6100 2150
Wire Wire Line
	8050 2200 7100 2200
Wire Wire Line
	7100 2000 7100 2200
Connection ~ 7100 2200
Wire Wire Line
	7100 2200 7100 2350
Wire Wire Line
	6950 3100 6950 3050
Wire Wire Line
	4250 3050 6950 3050
Wire Wire Line
	6950 3100 7300 3100
Wire Wire Line
	9400 2600 9400 2300
Text GLabel 1600 2350 2    50   Input ~ 0
GND
Text GLabel 1750 2600 0    50   Input ~ 0
GND
Wire Wire Line
	1750 2600 2000 2600
Wire Wire Line
	9200 2300 9400 2300
Connection ~ 9400 2300
Wire Wire Line
	9400 2300 9850 2300
Text GLabel 9400 3100 3    50   Input ~ 0
GND
Wire Wire Line
	9400 2900 9400 3100
Wire Wire Line
	7725 2400 8050 2400
Wire Wire Line
	7425 2400 7300 2400
Wire Wire Line
	7300 2400 7300 3100
Connection ~ 7300 3100
Wire Wire Line
	7300 3100 8700 3100
$EndSCHEMATC
