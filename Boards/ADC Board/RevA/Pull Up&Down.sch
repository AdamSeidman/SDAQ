EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 11
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
L Connector:Screw_Terminal_01x03 J3
U 1 1 615FC6ED
P 2150 1200
AR Path="/61593BCA/615FC6ED" Ref="J3"  Part="1" 
AR Path="/61640BD1/615FC6ED" Ref="J?"  Part="1" 
AR Path="/61641449/615FC6ED" Ref="J?"  Part="1" 
AR Path="/6164144B/615FC6ED" Ref="J?"  Part="1" 
AR Path="/616422A2/615FC6ED" Ref="J5"  Part="1" 
AR Path="/616423D2/615FC6ED" Ref="J7"  Part="1" 
AR Path="/616425FE/615FC6ED" Ref="J9"  Part="1" 
F 0 "J9" H 2500 950 50  0000 C CNN
F 1 "Screw Terminals" H 2550 1050 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 2150 1200 50  0001 C CNN
F 3 "~" H 2150 1200 50  0001 C CNN
	1    2150 1200
	-1   0    0    1   
$EndComp
Text HLabel 2500 850  2    50   Input ~ 0
5V
$Comp
L Device:R R1
U 1 1 616034B0
P 2950 1100
AR Path="/61593BCA/616034B0" Ref="R1"  Part="1" 
AR Path="/61640BD1/616034B0" Ref="R?"  Part="1" 
AR Path="/61641449/616034B0" Ref="R?"  Part="1" 
AR Path="/6164144B/616034B0" Ref="R?"  Part="1" 
AR Path="/616422A2/616034B0" Ref="R3"  Part="1" 
AR Path="/616423D2/616034B0" Ref="R5"  Part="1" 
AR Path="/616425FE/616034B0" Ref="R7"  Part="1" 
F 0 "R7" V 2743 1100 50  0000 C CNN
F 1 "10k" V 2834 1100 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2880 1100 50  0001 C CNN
F 3 "~" H 2950 1100 50  0001 C CNN
	1    2950 1100
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 61604CD1
P 2950 1300
AR Path="/61593BCA/61604CD1" Ref="R2"  Part="1" 
AR Path="/61640BD1/61604CD1" Ref="R?"  Part="1" 
AR Path="/61641449/61604CD1" Ref="R?"  Part="1" 
AR Path="/6164144B/61604CD1" Ref="R?"  Part="1" 
AR Path="/616422A2/61604CD1" Ref="R4"  Part="1" 
AR Path="/616423D2/61604CD1" Ref="R6"  Part="1" 
AR Path="/616425FE/61604CD1" Ref="R8"  Part="1" 
F 0 "R8" V 3150 1300 50  0000 C CNN
F 1 "10k" V 3050 1300 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2880 1300 50  0001 C CNN
F 3 "~" H 2950 1300 50  0001 C CNN
	1    2950 1300
	0    1    1    0   
$EndComp
Text HLabel 2500 1550 2    50   Input ~ 0
GND
Wire Wire Line
	2350 1100 2450 1100
Wire Wire Line
	2800 1300 2450 1300
$Comp
L Connector:Conn_01x03_Male J4
U 1 1 61613676
P 3750 1200
AR Path="/61593BCA/61613676" Ref="J4"  Part="1" 
AR Path="/61640BD1/61613676" Ref="J?"  Part="1" 
AR Path="/61641449/61613676" Ref="J?"  Part="1" 
AR Path="/6164144B/61613676" Ref="J?"  Part="1" 
AR Path="/616422A2/61613676" Ref="J6"  Part="1" 
AR Path="/616423D2/61613676" Ref="J8"  Part="1" 
AR Path="/616425FE/61613676" Ref="J10"  Part="1" 
F 0 "J10" H 3850 850 50  0000 R CNN
F 1 "Jumper Terminals" H 4100 950 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 3750 1200 50  0001 C CNN
F 3 "~" H 3750 1200 50  0001 C CNN
	1    3750 1200
	-1   0    0    1   
$EndComp
Wire Wire Line
	3100 1300 3550 1300
Wire Wire Line
	3100 1100 3550 1100
Wire Wire Line
	2350 1200 3550 1200
Wire Wire Line
	3550 1200 4000 1200
Connection ~ 3550 1200
Text HLabel 4000 1200 2    50   Input ~ 0
Digital_In
Wire Wire Line
	2500 1550 2450 1550
Wire Wire Line
	2450 1550 2450 1300
Connection ~ 2450 1300
Wire Wire Line
	2450 1300 2350 1300
Wire Wire Line
	2450 1100 2450 850 
Wire Wire Line
	2450 850  2500 850 
Connection ~ 2450 1100
Wire Wire Line
	2450 1100 2800 1100
$EndSCHEMATC
