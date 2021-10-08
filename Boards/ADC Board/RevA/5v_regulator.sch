EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 11 11
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
L Device:R_US R?
U 1 1 61653277
P 2550 2800
AR Path="/61653277" Ref="R?"  Part="1" 
AR Path="/6164E083/61653277" Ref="R?"  Part="1" 
AR Path="/61663709/61653277" Ref="R9"  Part="1" 
F 0 "R9" H 2618 2846 50  0000 L CNN
F 1 "350?" H 2618 2755 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2590 2790 50  0001 C CNN
F 3 "~" H 2550 2800 50  0001 C CNN
	1    2550 2800
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D?
U 1 1 6165327D
P 2550 3150
AR Path="/6165327D" Ref="D?"  Part="1" 
AR Path="/6164E083/6165327D" Ref="D?"  Part="1" 
AR Path="/61663709/6165327D" Ref="D1"  Part="1" 
F 0 "D1" V 2589 3032 50  0000 R CNN
F 1 "LED" V 2498 3032 50  0000 R CNN
F 2 "" H 2550 3150 50  0001 C CNN
F 3 "~" H 2550 3150 50  0001 C CNN
	1    2550 3150
	0    -1   -1   0   
$EndComp
Text HLabel 2550 2600 1    50   Input ~ 0
Vcc
Text HLabel 2550 3350 3    50   Input ~ 0
GND
$Comp
L Device:C C1
U 1 1 61655F33
P 3800 2300
F 0 "C1" H 3915 2346 50  0000 L CNN
F 1 "0.1uF" H 3915 2255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3838 2150 50  0001 C CNN
F 3 "~" H 3800 2300 50  0001 C CNN
	1    3800 2300
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 61656877
P 5950 2200
F 0 "C2" H 6065 2246 50  0000 L CNN
F 1 "1uF" H 6065 2155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5988 2050 50  0001 C CNN
F 3 "~" H 5950 2200 50  0001 C CNN
	1    5950 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 6165740F
P 6800 2250
F 0 "C3" H 6915 2296 50  0000 L CNN
F 1 "1uF_cpu" H 6915 2205 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6838 2100 50  0001 C CNN
F 3 "~" H 6800 2250 50  0001 C CNN
	1    6800 2250
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C4
U 1 1 6165888C
P 7450 2250
F 0 "C4" H 7568 2296 50  0000 L CNN
F 1 "4.7uF_16V_cpu" H 7568 2205 50  0000 L CNN
F 2 "" H 7488 2100 50  0001 C CNN
F 3 "~" H 7450 2250 50  0001 C CNN
	1    7450 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5950 2050 5950 2000
Wire Wire Line
	5950 2000 5550 2000
Text HLabel 5950 2400 3    50   Input ~ 0
GND
Text HLabel 3800 1850 1    50   Input ~ 0
Vcc
Text HLabel 3800 2500 3    50   Input ~ 0
GND
Wire Wire Line
	3800 2000 3800 1850
Wire Wire Line
	3800 2150 3800 2000
Connection ~ 3800 2000
Text HLabel 6800 2500 3    50   Input ~ 0
GND
Wire Wire Line
	6800 2500 6800 2400
Wire Wire Line
	5950 2000 6500 2000
Wire Wire Line
	6800 2000 6800 2100
Connection ~ 5950 2000
Wire Wire Line
	6800 2100 7450 2100
Connection ~ 6800 2100
Wire Wire Line
	6800 2400 7450 2400
Connection ~ 6800 2400
Text HLabel 4350 2250 3    50   Input ~ 0
GND
Text HLabel 6500 1950 1    50   Input ~ 0
5V
Wire Wire Line
	3800 2500 3800 2450
Wire Wire Line
	4350 2250 4350 2200
Wire Wire Line
	5950 2400 5950 2350
Wire Wire Line
	2550 3000 2550 2950
Wire Wire Line
	2550 3350 2550 3300
Wire Wire Line
	2550 2600 2550 2650
Wire Wire Line
	6500 1950 6500 2000
Connection ~ 6500 2000
Wire Wire Line
	6500 2000 6800 2000
Wire Wire Line
	3800 2000 4350 2000
$Comp
L LM1117IMPX-5.0:LM1117IMPX-5.0 VR1
U 1 1 6168283C
P 4950 2100
AR Path="/6168283C" Ref="VR1"  Part="1" 
AR Path="/61663709/6168283C" Ref="VR1"  Part="1" 
F 0 "VR1" H 4950 2467 50  0000 C CNN
F 1 "LM1117IMPX-5.0" H 4950 2376 50  0000 C CNN
F 2 "" H 4950 2100 50  0001 L BNN
F 3 "1.80 mm" H 4950 2100 50  0001 L BNN
F 4 "O" H 4950 2100 50  0001 L BNN "Field4"
F 5 "IPC 7351B" H 4950 2100 50  0001 L BNN "Field5"
F 6 "Rochester Electronics/Texas Instruments" H 4950 2100 50  0001 L BNN "Field6"
	1    4950 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 2000 5550 2200
Connection ~ 5550 2000
$EndSCHEMATC
