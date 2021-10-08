EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
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
S 7750 3550 700  500 
U 61593BCA
F0 "Pull Up&Down 0" 50
F1 "Pull Up&Down.sch" 50
F2 "5V" I L 7750 3650 50 
F3 "GND" I L 7750 3800 50 
F4 "Digital_In" I L 7750 3950 50 
$EndSheet
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 615E5E26
P 1600 1850
F 0 "J?" H 1650 2467 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 1650 2376 50  0000 C CNN
F 2 "" H 1600 1850 50  0001 C CNN
F 3 "~" H 1600 1850 50  0001 C CNN
	1    1600 1850
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x12_Counter_Clockwise J?
U 1 1 615E7214
P 3000 1850
F 0 "J?" H 3050 2567 50  0000 C CNN
F 1 "Conn_02x12_Counter_Clockwise" H 3050 2476 50  0000 C CNN
F 2 "" H 3000 1850 50  0001 C CNN
F 3 "~" H 3000 1850 50  0001 C CNN
	1    3000 1850
	1    0    0    -1  
$EndComp
Text Label 1400 1450 2    50   ~ 0
3.3V
Text Label 1400 1550 2    50   ~ 0
5V
Text Label 1400 1750 2    50   ~ 0
5V
Text Label 1400 1850 2    50   ~ 0
GND
Text Label 1400 2250 2    50   ~ 0
GND
$Sheet
S 9200 3550 700  500 
U 616422A2
F0 "Pull Up&Down 1" 50
F1 "Pull Up&Down.sch" 50
F2 "5V" I L 9200 3650 50 
F3 "GND" I L 9200 3800 50 
F4 "Digital_In" I L 9200 3950 50 
$EndSheet
$Sheet
S 7750 4300 700  500 
U 616423D2
F0 "Pull Up&Down 2" 50
F1 "Pull Up&Down.sch" 50
F2 "5V" I L 7750 4400 50 
F3 "GND" I L 7750 4550 50 
F4 "Digital_In" I L 7750 4700 50 
$EndSheet
$Sheet
S 9200 4300 700  500 
U 616425FE
F0 "Pull Up&Down 3" 50
F1 "Pull Up&Down.sch" 50
F2 "5V" I L 9200 4400 50 
F3 "GND" I L 9200 4550 50 
F4 "Digital_In" I L 9200 4700 50 
$EndSheet
Text Label 7750 3650 2    50   ~ 0
5V
Text Label 7750 3800 2    50   ~ 0
GND
Text Label 7750 4400 2    50   ~ 0
5V
Text Label 7750 4550 2    50   ~ 0
GND
Text Label 9200 4400 2    50   ~ 0
5V
Text Label 9200 4550 2    50   ~ 0
GND
Text Label 9200 3650 2    50   ~ 0
5V
Text Label 9200 3800 2    50   ~ 0
GND
$Sheet
S 4550 1300 2500 1800
U 6158C434
F0 "Controller" 50
F1 "controller.sch" 50
F2 "GND" I R 7050 1600 50 
F3 "5V" I R 7050 1750 50 
F4 "Reset" I L 4550 1550 50 
F5 "I2C_Clock" B L 4550 2000 50 
F6 "I2C_Data" B L 4550 2150 50 
F7 "Digital_2" I R 7050 2250 50 
F8 "Digital_1" I R 7050 2100 50 
F9 "Digital_3" I R 7050 2400 50 
F10 "Digital_0" I R 7050 1950 50 
F11 "Analog_0" I R 7050 2550 50 
F12 "Analog_1" I R 7050 2700 50 
F13 "Analog_2" I R 7050 2850 50 
F14 "Analog_3" I R 7050 3000 50 
$EndSheet
Text Label 7750 3950 2    50   ~ 0
Digital_0
Text Label 9200 3950 2    50   ~ 0
Digital_1
Text Label 7750 4700 2    50   ~ 0
Digital_2
Text Label 9200 4700 2    50   ~ 0
Digital_3
Text Label 7050 1950 0    50   ~ 0
Digital_0
Text Label 7050 2100 0    50   ~ 0
Digital_1
Text Label 7050 2250 0    50   ~ 0
Digital_2
$EndSCHEMATC