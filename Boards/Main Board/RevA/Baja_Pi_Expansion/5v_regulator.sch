EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
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
F 0 "R?" H 2618 2846 50  0000 L CNN
F 1 "R_US" H 2618 2755 50  0000 L CNN
F 2 "" V 2590 2790 50  0001 C CNN
F 3 "~" H 2550 2800 50  0001 C CNN
	1    2550 2800
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D?
U 1 1 6165327D
P 2550 3100
AR Path="/6165327D" Ref="D?"  Part="1" 
AR Path="/6164E083/6165327D" Ref="D?"  Part="1" 
F 0 "D?" V 2589 2982 50  0000 R CNN
F 1 "LED" V 2498 2982 50  0000 R CNN
F 2 "" H 2550 3100 50  0001 C CNN
F 3 "~" H 2550 3100 50  0001 C CNN
	1    2550 3100
	0    -1   -1   0   
$EndComp
Text HLabel 2550 2650 1    50   Input ~ 0
Vcc
Text HLabel 2550 3250 3    50   Input ~ 0
GND
$Comp
L Regulator_Linear:LM1117-5.0 U?
U 1 1 616546A9
P 4750 2850
F 0 "U?" H 4750 3092 50  0000 C CNN
F 1 "LM1117-5.0" H 4750 3001 50  0000 C CNN
F 2 "" H 4750 2850 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm1117.pdf" H 4750 2850 50  0001 C CNN
	1    4750 2850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
