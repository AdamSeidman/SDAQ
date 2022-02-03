EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Label 1700 1350 2    50   ~ 0
3v3
Text Label 2200 1650 0    50   ~ 0
3v3
Text Label 1700 1450 2    50   ~ 0
5v
Text Label 1700 1650 2    50   ~ 0
5v
Text Label 1700 2150 2    50   ~ 0
gnd
Text Label 4100 5200 2    50   ~ 0
gnd
Text Label 4600 5300 0    50   ~ 0
gnd
Text Label 1700 1850 2    50   ~ 0
gnd
Text Label 2200 1950 0    50   ~ 0
gnd
Text Label 2200 1350 0    50   ~ 0
gnd
Text Label 4100 5700 2    50   ~ 0
gnd
Text Label 4600 5800 0    50   ~ 0
gnd
Text Label 4100 5400 2    50   ~ 0
sda
Text Label 4100 5500 2    50   ~ 0
scl
Text Label 4100 5000 2    50   ~ 0
sclk
Text Label 4100 4800 2    50   ~ 0
miso
Text Label 2200 1450 0    50   ~ 0
mosi
Text Label 4100 5100 2    50   ~ 0
spi_ce0
Text Label 4100 5300 2    50   ~ 0
spi_ce1
Text Label 1700 1550 2    50   ~ 0
sda2
Text Label 1700 1750 2    50   ~ 0
scl2
Text Label 1700 2050 2    50   ~ 0
uart_tx
Text Label 1700 2250 2    50   ~ 0
uart_rx
Text Label 4600 5200 0    50   ~ 0
sclk2
Text Label 4600 5400 0    50   ~ 0
miso2
Text Label 4600 5600 0    50   ~ 0
spi2_ce2
Text Label 4600 5700 0    50   ~ 0
miso2_pwm
Text Label 1700 1950 2    50   ~ 0
gpio1
Text Label 4100 5600 2    50   ~ 0
gpio2
Text Label 4100 5800 2    50   ~ 0
gpio3
Text Label 4100 5900 2    50   ~ 0
gpio4
Text Label 4600 5900 0    50   ~ 0
gpio5
Text Label 2200 1850 0    50   ~ 0
gpio6
Text Label 2200 1750 0    50   ~ 0
gpio7
Text Label 2200 1550 0    50   ~ 0
gpio8
Text Label 4100 4900 2    50   ~ 0
gpio9
Text Label 4600 5500 0    50   ~ 0
gpio10
Text Label 2200 2050 0    50   ~ 0
gpio11
Text Label 2200 2250 0    50   ~ 0
spi2_ce1
Text Label 2200 2150 0    50   ~ 0
spi2_ce0
Text Notes 1450 1950 2    50   ~ 0
4
Text Notes 2500 2050 0    50   ~ 0
27
Text Notes 2450 1850 0    50   ~ 0
22
Text Notes 3800 5600 2    50   ~ 0
5
Text Notes 3800 5800 2    50   ~ 0
6
Text Notes 4900 5900 0    50   ~ 0
13
Text Notes 5050 5900 0    50   ~ 0
pwm
Text Notes 4900 5500 0    50   ~ 0
26
Text Notes 1100 2050 0    50   ~ 0
gpio 14
Text Notes 1400 2250 2    50   ~ 0
gpio 15
Text Notes 2550 2250 0    50   ~ 0
gpio 17
Text Notes 2750 2150 2    50   ~ 0
pwm
Text Notes 2550 1750 2    50   ~ 0
23
Text Notes 2550 1550 2    50   ~ 0
24
Text Notes 3750 4900 0    50   ~ 0
25
Text Notes 3550 5100 0    50   ~ 0
gpio 8
Text Notes 3500 5300 0    50   ~ 0
gpio 7
Text Notes 3700 5500 0    50   ~ 0
gpio 1
Text Notes 3550 5900 0    50   ~ 0
12 pwm
Text Notes 5300 5600 2    50   ~ 0
gpio 16
Text Notes 5200 5400 2    50   ~ 0
gpio 20
Text Notes 5150 5200 2    50   ~ 0
gpio 21
Text Notes 3900 5000 2    50   ~ 0
gpio 11
Text Notes 3900 5400 2    50   ~ 0
gpio 0
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J1
U 1 1 6160E35B
P 1900 1750
F 0 "J1" H 1950 2367 50  0000 C CNN
F 1 "main_conn_10" H 1950 2276 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 1900 1750 50  0001 C CNN
F 3 "~" H 1900 1750 50  0001 C CNN
	1    1900 1750
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x12_Counter_Clockwise J2
U 1 1 6160FED6
P 4300 5300
F 0 "J2" H 4350 6017 50  0000 C CNN
F 1 "main_conn_12" H 4350 5926 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 4300 5300 50  0001 C CNN
F 3 "~" H 4300 5300 50  0001 C CNN
	1    4300 5300
	1    0    0    -1  
$EndComp
Text Label 4600 5000 0    50   ~ 0
reset
Text Notes 2700 1450 2    50   ~ 0
gpio 10
Text Notes 3900 4800 2    50   ~ 0
gpio 9
Text Notes 4400 6050 2    50   ~ 0
+20
Text Label 4600 4800 0    50   ~ 0
vcc
Text Label 4600 4900 0    50   ~ 0
vcc
$Comp
L Device:R_US R5
U 1 1 61FC7A2D
P 1250 3550
AR Path="/61FC7A2D" Ref="R5"  Part="1" 
AR Path="/6164E083/61FC7A2D" Ref="R?"  Part="1" 
F 0 "R5" H 1318 3596 50  0000 L CNN
F 1 "350?" H 1318 3505 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1290 3540 50  0001 C CNN
F 3 "~" H 1250 3550 50  0001 C CNN
	1    1250 3550
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D1
U 1 1 61FC7A33
P 1250 3900
AR Path="/61FC7A33" Ref="D1"  Part="1" 
AR Path="/6164E083/61FC7A33" Ref="D?"  Part="1" 
F 0 "D1" V 1289 3782 50  0000 R CNN
F 1 "LED" V 1198 3782 50  0000 R CNN
F 2 "LED_SMD:LED_1812_4532Metric" H 1250 3900 50  0001 C CNN
F 3 "~" H 1250 3900 50  0001 C CNN
	1    1250 3900
	0    -1   -1   0   
$EndComp
Text HLabel 1250 3350 1    50   Input ~ 0
Vcc
Text HLabel 1250 4100 3    50   Input ~ 0
GND
Wire Wire Line
	1250 3750 1250 3700
Wire Wire Line
	1250 4100 1250 4050
Wire Wire Line
	1250 3350 1250 3400
Text Label 7550 5250 2    50   ~ 0
gnd
Text Label 9800 5350 2    50   ~ 0
gnd
Text Label 7550 5750 2    50   ~ 0
gnd
Text Label 9800 5850 2    50   ~ 0
gnd
Text Label 7550 5450 2    50   ~ 0
sda
Text Label 7550 5550 2    50   ~ 0
scl
Text Label 7550 5050 2    50   ~ 0
sclk
Text Label 7550 4850 2    50   ~ 0
miso
Text Label 7550 5150 2    50   ~ 0
spi_ce0
Text Label 7550 5350 2    50   ~ 0
spi_ce1
Text Label 9800 5250 2    50   ~ 0
sclk2
Text Label 9800 5450 2    50   ~ 0
miso2
Text Label 9800 5650 2    50   ~ 0
spi2_ce2
Text Label 9800 5750 2    50   ~ 0
miso2_pwm
Text Label 7550 5650 2    50   ~ 0
gpio2
Text Label 7550 5850 2    50   ~ 0
gpio3
Text Label 7550 5950 2    50   ~ 0
gpio4
Text Label 9800 5950 2    50   ~ 0
gpio5
Text Label 7550 4950 2    50   ~ 0
gpio9
Text Label 9800 5550 2    50   ~ 0
gpio10
Text Notes 7250 5650 2    50   ~ 0
5
Text Notes 7250 5850 2    50   ~ 0
6
Text Notes 9500 5950 2    50   ~ 0
13
Text Notes 9350 5950 2    50   ~ 0
pwm
Text Notes 9500 5550 2    50   ~ 0
26
Text Notes 7200 4950 0    50   ~ 0
25
Text Notes 7000 5150 0    50   ~ 0
gpio 8
Text Notes 6950 5350 0    50   ~ 0
gpio 7
Text Notes 7150 5550 0    50   ~ 0
gpio 1
Text Notes 7000 5950 0    50   ~ 0
12 pwm
Text Notes 9100 5650 0    50   ~ 0
gpio 16
Text Notes 9200 5450 0    50   ~ 0
gpio 20
Text Notes 9250 5250 0    50   ~ 0
gpio 21
Text Notes 7350 5050 2    50   ~ 0
gpio 11
Text Notes 7350 5450 2    50   ~ 0
gpio 0
$Comp
L Connector_Generic:Conn_02x12_Counter_Clockwise J?
U 1 1 61FD1A5A
P 7750 5350
F 0 "J?" H 7800 6067 50  0000 C CNN
F 1 "Conn_02x12_Counter_Clockwise" H 7800 5976 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 7750 5350 50  0001 C CNN
F 3 "~" H 7750 5350 50  0001 C CNN
	1    7750 5350
	1    0    0    -1  
$EndComp
Text Label 9800 5050 2    50   ~ 0
reset
Text Notes 7350 4850 2    50   ~ 0
gpio 9
Text Notes 7850 6100 2    50   ~ 0
+20
Text Label 9800 4850 2    50   ~ 0
vcc
Text Label 9800 4950 2    50   ~ 0
vcc
Text Label 8050 5250 0    50   ~ 0
gnd
Text Label 10300 5350 0    50   ~ 0
gnd
Text Label 8050 5750 0    50   ~ 0
gnd
Text Label 10300 5850 0    50   ~ 0
gnd
Text Label 8050 5450 0    50   ~ 0
sda
Text Label 8050 5550 0    50   ~ 0
scl
Text Label 8050 5050 0    50   ~ 0
sclk
Text Label 8050 4850 0    50   ~ 0
miso
Text Label 8050 5150 0    50   ~ 0
spi_ce0
Text Label 8050 5350 0    50   ~ 0
spi_ce1
Text Label 10300 5250 0    50   ~ 0
sclk2
Text Label 10300 5450 0    50   ~ 0
miso2
Text Label 10300 5650 0    50   ~ 0
spi2_ce2
Text Label 10300 5750 0    50   ~ 0
miso2_pwm
Text Label 8050 5650 0    50   ~ 0
gpio2
Text Label 8050 5850 0    50   ~ 0
gpio3
Text Label 8050 5950 0    50   ~ 0
gpio4
Text Label 10300 5950 0    50   ~ 0
gpio5
Text Label 8050 4950 0    50   ~ 0
gpio9
Text Label 10300 5550 0    50   ~ 0
gpio10
Text Notes 8350 5650 0    50   ~ 0
5
Text Notes 8350 5850 0    50   ~ 0
6
Text Notes 10600 5950 0    50   ~ 0
13
Text Notes 10750 5950 0    50   ~ 0
pwm
Text Notes 10600 5550 0    50   ~ 0
26
Text Notes 8400 4950 2    50   ~ 0
25
Text Notes 8600 5150 2    50   ~ 0
gpio 8
Text Notes 8650 5350 2    50   ~ 0
gpio 7
Text Notes 8450 5550 2    50   ~ 0
gpio 1
Text Notes 8600 5950 2    50   ~ 0
12 pwm
Text Notes 11000 5650 2    50   ~ 0
gpio 16
Text Notes 10900 5450 2    50   ~ 0
gpio 20
Text Notes 10850 5250 2    50   ~ 0
gpio 21
Text Notes 8250 5050 0    50   ~ 0
gpio 11
Text Notes 8250 5450 0    50   ~ 0
gpio 0
$Comp
L Connector_Generic:Conn_02x12_Counter_Clockwise J?
U 1 1 61FD41D1
P 10000 5350
F 0 "J?" H 10050 6067 50  0000 C CNN
F 1 "Conn_02x12_Counter_Clockwise" H 10050 5976 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 10000 5350 50  0001 C CNN
F 3 "~" H 10000 5350 50  0001 C CNN
	1    10000 5350
	1    0    0    -1  
$EndComp
Text Label 10300 5050 0    50   ~ 0
reset
Text Notes 8250 4850 0    50   ~ 0
gpio 9
Text Notes 10100 6100 2    50   ~ 0
+20
Text Label 10300 4850 0    50   ~ 0
vcc
Text Label 10300 4950 0    50   ~ 0
vcc
Text Label 4600 5100 0    50   ~ 0
NC
Text Label 9800 5150 2    50   ~ 0
NC
Text Label 10300 5150 0    50   ~ 0
NC
Text Label 5400 1300 2    50   ~ 0
3v3
Text Label 7550 1600 2    50   ~ 0
3v3
Text Label 5400 1400 2    50   ~ 0
5v
Text Label 5400 1600 2    50   ~ 0
5v
Text Label 5400 2100 2    50   ~ 0
gnd
Text Label 5400 1800 2    50   ~ 0
gnd
Text Label 7550 1900 2    50   ~ 0
gnd
Text Label 7550 1300 2    50   ~ 0
gnd
Text Label 7550 1400 2    50   ~ 0
mosi
Text Label 5400 1500 2    50   ~ 0
sda2
Text Label 5400 1700 2    50   ~ 0
scl2
Text Label 5400 2000 2    50   ~ 0
uart_tx
Text Label 5400 2200 2    50   ~ 0
uart_rx
Text Label 5400 1900 2    50   ~ 0
gpio1
Text Label 7550 1800 2    50   ~ 0
gpio6
Text Label 7550 1700 2    50   ~ 0
gpio7
Text Label 7550 1500 2    50   ~ 0
gpio8
Text Label 7550 2000 2    50   ~ 0
gpio11
Text Label 7550 2200 2    50   ~ 0
spi2_ce1
Text Label 7550 2100 2    50   ~ 0
spi2_ce0
Text Notes 5150 1900 2    50   ~ 0
4
Text Notes 7250 2000 2    50   ~ 0
27
Text Notes 7300 1800 2    50   ~ 0
22
Text Notes 4800 2000 0    50   ~ 0
gpio 14
Text Notes 5100 2200 2    50   ~ 0
gpio 15
Text Notes 7200 2200 2    50   ~ 0
gpio 17
Text Notes 7000 2100 0    50   ~ 0
pwm
Text Notes 7200 1700 0    50   ~ 0
23
Text Notes 7200 1500 0    50   ~ 0
24
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 61FF84C4
P 5600 1700
F 0 "J?" H 5650 2317 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 5650 2226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 5600 1700 50  0001 C CNN
F 3 "~" H 5600 1700 50  0001 C CNN
	1    5600 1700
	1    0    0    -1  
$EndComp
Text Notes 7050 1400 0    50   ~ 0
gpio 10
Text Label 5900 1300 0    50   ~ 0
3v3
Text Label 8050 1600 0    50   ~ 0
3v3
Text Label 5900 1400 0    50   ~ 0
5v
Text Label 5900 1600 0    50   ~ 0
5v
Text Label 5900 2100 0    50   ~ 0
gnd
Text Label 5900 1800 0    50   ~ 0
gnd
Text Label 8050 1900 0    50   ~ 0
gnd
Text Label 8050 1300 0    50   ~ 0
gnd
Text Label 8050 1400 0    50   ~ 0
mosi
Text Label 5900 1500 0    50   ~ 0
sda2
Text Label 5900 1700 0    50   ~ 0
scl2
Text Label 5900 2000 0    50   ~ 0
uart_tx
Text Label 5900 2200 0    50   ~ 0
uart_rx
Text Label 5900 1900 0    50   ~ 0
gpio1
Text Label 8050 1800 0    50   ~ 0
gpio6
Text Label 8050 1700 0    50   ~ 0
gpio7
Text Label 8050 1500 0    50   ~ 0
gpio8
Text Label 8050 2000 0    50   ~ 0
gpio11
Text Label 8050 2200 0    50   ~ 0
spi2_ce1
Text Label 8050 2100 0    50   ~ 0
spi2_ce0
Text Notes 6150 1900 0    50   ~ 0
4
Text Notes 8350 2000 0    50   ~ 0
27
Text Notes 8300 1800 0    50   ~ 0
22
Text Notes 6500 2000 2    50   ~ 0
gpio 14
Text Notes 6200 2200 0    50   ~ 0
gpio 15
Text Notes 8400 2200 0    50   ~ 0
gpio 17
Text Notes 8600 2100 2    50   ~ 0
pwm
Text Notes 8400 1700 2    50   ~ 0
23
Text Notes 8400 1500 2    50   ~ 0
24
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 61FFAAA2
P 7750 1700
F 0 "J?" H 7800 2317 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 7800 2226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 7750 1700 50  0001 C CNN
F 3 "~" H 7750 1700 50  0001 C CNN
	1    7750 1700
	1    0    0    -1  
$EndComp
Text Notes 8550 1400 2    50   ~ 0
gpio 10
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 62008AB1
P 3050 3200
F 0 "J?" H 3100 3817 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 3100 3726 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 3050 3200 50  0001 C CNN
F 3 "~" H 3050 3200 50  0001 C CNN
	1    3050 3200
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x10_Counter_Clockwise J?
U 1 1 6200A2AB
P 3850 3200
F 0 "J?" H 3900 3817 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 3900 3726 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 3850 3200 50  0001 C CNN
F 3 "~" H 3850 3200 50  0001 C CNN
	1    3850 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 2800 3350 2800
Wire Wire Line
	3650 2800 3350 2800
Connection ~ 3350 2800
Wire Wire Line
	3650 2800 4150 2800
Connection ~ 3650 2800
Wire Wire Line
	4150 2900 3650 2900
Wire Wire Line
	3650 2900 3350 2900
Connection ~ 3650 2900
Wire Wire Line
	3350 2900 2850 2900
Connection ~ 3350 2900
Wire Wire Line
	2850 3000 3350 3000
Wire Wire Line
	3650 3000 3350 3000
Connection ~ 3350 3000
Wire Wire Line
	3650 3000 4150 3000
Connection ~ 3650 3000
Wire Wire Line
	4150 3100 3650 3100
Wire Wire Line
	3650 3100 3350 3100
Connection ~ 3650 3100
Wire Wire Line
	3350 3100 2850 3100
Connection ~ 3350 3100
Wire Wire Line
	2850 3200 3350 3200
Wire Wire Line
	3650 3200 3350 3200
Connection ~ 3350 3200
Wire Wire Line
	3650 3200 4150 3200
Connection ~ 3650 3200
Wire Wire Line
	4150 3300 3650 3300
Wire Wire Line
	2850 3300 3350 3300
Wire Wire Line
	3350 3300 3650 3300
Connection ~ 3350 3300
Connection ~ 3650 3300
Wire Wire Line
	4150 3400 3650 3400
Wire Wire Line
	3650 3400 3350 3400
Connection ~ 3650 3400
Wire Wire Line
	3350 3400 2850 3400
Connection ~ 3350 3400
Wire Wire Line
	2850 3500 3350 3500
Wire Wire Line
	3650 3500 3350 3500
Connection ~ 3350 3500
Wire Wire Line
	3650 3500 4150 3500
Connection ~ 3650 3500
Wire Wire Line
	4150 3600 3650 3600
Wire Wire Line
	3350 3600 2850 3600
Wire Wire Line
	3350 3600 3650 3600
Connection ~ 3350 3600
Connection ~ 3650 3600
Wire Wire Line
	4150 3700 3650 3700
Wire Wire Line
	3650 3700 3350 3700
Connection ~ 3650 3700
Wire Wire Line
	3350 3700 2850 3700
Connection ~ 3350 3700
$Comp
L Mechanical:MountingHole H?
U 1 1 620171F6
P 5600 3300
F 0 "H?" H 5700 3346 50  0000 L CNN
F 1 "CMH" H 5700 3255 50  0000 L CNN
F 2 "" H 5600 3300 50  0001 C CNN
F 3 "~" H 5600 3300 50  0001 C CNN
	1    5600 3300
	1    0    0    -1  
$EndComp
$EndSCHEMATC
