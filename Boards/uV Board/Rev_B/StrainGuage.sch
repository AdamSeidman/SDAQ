EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 2450 1150 0    50   ~ 0
Hemobllo Strain Guage
Text HLabel 3250 1550 0    50   Input ~ 0
5V
Text HLabel 3250 1350 0    50   Input ~ 0
GND
Text HLabel 3200 1450 0    50   Input ~ 0
Strain_Out
$Comp
L Connector:Conn_01x03_Female J9
U 1 1 61602119
P 3450 1450
AR Path="/614FDE40/61602119" Ref="J9"  Part="1" 
AR Path="/6153C564/61602119" Ref="J6"  Part="1" 
AR Path="/61575905/61602119" Ref="J8"  Part="1" 
AR Path="/61575900/61602119" Ref="J7"  Part="1" 
F 0 "J9" H 3478 1476 50  0000 L CNN
F 1 "Conn_01x03_Female" H 3478 1385 50  0000 L CNN
F 2 "" H 3450 1450 50  0001 C CNN
F 3 "~" H 3450 1450 50  0001 C CNN
	1    3450 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3200 1450 3250 1450
$Comp
L Connector:Conn_01x02_Female J10
U 1 1 615FC90F
P 2000 1700
AR Path="/6153C564/615FC90F" Ref="J10"  Part="1" 
AR Path="/61575900/615FC90F" Ref="J11"  Part="1" 
AR Path="/61575905/615FC90F" Ref="J12"  Part="1" 
AR Path="/614FDE40/615FC90F" Ref="J13"  Part="1" 
F 0 "J13" H 2028 1676 50  0000 L CNN
F 1 "Conn_01x02_Female" H 2028 1585 50  0000 L CNN
F 2 "" H 2000 1700 50  0001 C CNN
F 3 "~" H 2000 1700 50  0001 C CNN
	1    2000 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 1700 1800 1700
Wire Wire Line
	1800 1800 1700 1800
Text Label 1700 1700 2    50   ~ 0
Strain_In_High
Text Label 1700 1800 2    50   ~ 0
Strain_In_Low
$Comp
L Connector:Conn_01x02_Female J14
U 1 1 61600C0D
P 2000 2000
AR Path="/6153C564/61600C0D" Ref="J14"  Part="1" 
AR Path="/61575900/61600C0D" Ref="J15"  Part="1" 
AR Path="/61575905/61600C0D" Ref="J16"  Part="1" 
AR Path="/614FDE40/61600C0D" Ref="J17"  Part="1" 
F 0 "J17" H 2028 1976 50  0000 L CNN
F 1 "Conn_01x02_Female" H 2028 1885 50  0000 L CNN
F 2 "" H 2000 2000 50  0001 C CNN
F 3 "~" H 2000 2000 50  0001 C CNN
	1    2000 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 2000 1800 2000
Wire Wire Line
	1800 2100 1700 2100
Text Label 1700 2000 2    50   ~ 0
Strain_In_High
Text Label 1700 2100 2    50   ~ 0
Strain_In_Low
$EndSCHEMATC
