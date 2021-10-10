EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 10 11
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
L Connector:Screw_Terminal_01x03 J?
U 1 1 61653B35
P 1650 1300
AR Path="/61593BCA/61653B35" Ref="J?"  Part="1" 
AR Path="/61640BD1/61653B35" Ref="J?"  Part="1" 
AR Path="/61641449/61653B35" Ref="J?"  Part="1" 
AR Path="/6164144B/61653B35" Ref="J?"  Part="1" 
AR Path="/616422A2/61653B35" Ref="J?"  Part="1" 
AR Path="/616423D2/61653B35" Ref="J?"  Part="1" 
AR Path="/616425FE/61653B35" Ref="J?"  Part="1" 
AR Path="/6164D83E/61653B35" Ref="J14"  Part="1" 
AR Path="/616568DC/61653B35" Ref="J15"  Part="1" 
AR Path="/61657053/61653B35" Ref="J16"  Part="1" 
AR Path="/616571E9/61653B35" Ref="J17"  Part="1" 
F 0 "J17" H 2000 1050 50  0000 C CNN
F 1 "Screw Terminals" H 2050 1150 50  0000 C CNN
F 2 "" H 1650 1300 50  0001 C CNN
F 3 "~" H 1650 1300 50  0001 C CNN
	1    1650 1300
	-1   0    0    1   
$EndComp
Text HLabel 2000 950  2    50   Input ~ 0
5V
Text HLabel 2000 1650 2    50   Input ~ 0
GND
Wire Wire Line
	1850 1200 1950 1200
Wire Wire Line
	2000 1650 1950 1650
Wire Wire Line
	1950 1650 1950 1400
Wire Wire Line
	1950 1400 1850 1400
Wire Wire Line
	1950 1200 1950 950 
Wire Wire Line
	1950 950  2000 950 
Text HLabel 2250 1300 2    50   Input ~ 0
Analog_Input
Wire Wire Line
	1850 1300 2250 1300
$EndSCHEMATC
