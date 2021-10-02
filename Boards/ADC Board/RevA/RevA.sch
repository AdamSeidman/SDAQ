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
$Sheet
S 4550 1300 2500 1700
U 6158C434
F0 "Controller" 50
F1 "controller.sch" 50
F2 "GND" I R 7050 1600 50 
F3 "5V" I R 7050 1750 50 
F4 "Reset" I L 4550 1550 50 
F5 "I2C_Clock" B L 4550 2000 50 
F6 "I2C_Data" B L 4550 2150 50 
$EndSheet
Text Label 7050 1600 0    50   ~ 0
GND
Text Label 7050 1750 0    50   ~ 0
5V
Text Label 5400 900  0    50   ~ 0
GND
Text Label 5750 900  0    50   ~ 0
5V
$Comp
L power:+5V #PWR?
U 1 1 6158EB64
P 5750 700
F 0 "#PWR?" H 5750 550 50  0001 C CNN
F 1 "+5V" H 5765 873 50  0000 C CNN
F 2 "" H 5750 700 50  0001 C CNN
F 3 "" H 5750 700 50  0001 C CNN
	1    5750 700 
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 700  5750 900 
$Comp
L power:GNDREF #PWR?
U 1 1 6158F66D
P 5400 600
F 0 "#PWR?" H 5400 350 50  0001 C CNN
F 1 "GNDREF" H 5405 427 50  0000 C CNN
F 2 "" H 5400 600 50  0001 C CNN
F 3 "" H 5400 600 50  0001 C CNN
	1    5400 600 
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 600  5400 900 
Text Label 6050 900  0    50   ~ 0
3.3V
$Comp
L power:+3.3V #PWR?
U 1 1 615902F5
P 6050 700
F 0 "#PWR?" H 6050 550 50  0001 C CNN
F 1 "+3.3V" H 6065 873 50  0000 C CNN
F 2 "" H 6050 700 50  0001 C CNN
F 3 "" H 6050 700 50  0001 C CNN
	1    6050 700 
	1    0    0    -1  
$EndComp
Wire Wire Line
	6050 700  6050 900 
$Sheet
S 7750 3550 2500 1650
U 61593BCA
F0 "Pull Up&Down" 50
F1 "Pull Up&Down.sch" 50
$EndSheet
$Sheet
S 7750 1300 2450 1700
U 6159480C
F0 "Button Inputs" 50
F1 "Button Inputs.sch" 50
$EndSheet
$EndSCHEMATC
