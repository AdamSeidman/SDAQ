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
3v3_2
Text Label 1700 1450 2    50   ~ 0
5v
Text Label 1700 1650 2    50   ~ 0
5v2
Text Label 1700 2150 2    50   ~ 0
gnd2
Text Label 4100 5200 2    50   ~ 0
gnd_3
Text Label 4600 5300 0    50   ~ 0
gnd_
Text Label 1700 1850 2    50   ~ 0
gnd
Text Label 2200 1950 0    50   ~ 0
gnd3
Text Label 2200 1350 0    50   ~ 0
gnd4
Text Label 4100 5700 2    50   ~ 0
gnd_2
Text Label 4600 5800 0    50   ~ 0
gnd_1
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
L Connector_Generic:Conn_02x10_Odd_Even J1
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
L Connector_Generic:Conn_02x12_Odd_Even J2
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
Text Label 4600 4900 0    50   ~ 0
vcc
Text Notes 7850 6100 2    50   ~ 0
+20
$Comp
L Connector_Generic:Conn_02x12_Odd_Even J12
U 1 1 61FD41D1
P 10000 5350
F 0 "J12" H 10050 6067 50  0000 C CNN
F 1 "Conn_02x12_Counter_Clockwise" H 10050 5976 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 10000 5350 50  0001 C CNN
F 3 "~" H 10000 5350 50  0001 C CNN
	1    10000 5350
	1    0    0    -1  
$EndComp
Text Notes 10100 6100 2    50   ~ 0
+20
Text Label 4600 5100 0    50   ~ 0
NC
$Comp
L Connector_Generic:Conn_02x10_Odd_Even J5
U 1 1 61FF84C4
P 5600 1700
F 0 "J5" H 5650 2317 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 5650 2226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 5600 1700 50  0001 C CNN
F 3 "~" H 5600 1700 50  0001 C CNN
	1    5600 1700
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x10_Odd_Even J8
U 1 1 61FFAAA2
P 7750 1700
F 0 "J8" H 7800 2317 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 7800 2226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 7750 1700 50  0001 C CNN
F 3 "~" H 7750 1700 50  0001 C CNN
	1    7750 1700
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x10_Odd_Even J3
U 1 1 62008AB1
P 3050 3200
F 0 "J3" H 3100 3817 50  0000 C CNN
F 1 "Conn_02x10_Counter_Clockwise" H 3100 3726 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x10_P2.54mm_Vertical" H 3050 3200 50  0001 C CNN
F 3 "~" H 3050 3200 50  0001 C CNN
	1    3050 3200
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x10_Odd_Even J4
U 1 1 6200A2AB
P 3850 3200
F 0 "J4" H 3900 3817 50  0000 C CNN
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
L Mechanical:MountingHole H1
U 1 1 620171F6
P 1150 4900
F 0 "H1" H 1250 4946 50  0000 L CNN
F 1 "CMH" H 1250 4855 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 1150 4900 50  0001 C CNN
F 3 "~" H 1150 4900 50  0001 C CNN
	1    1150 4900
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x15_Odd_Even J6
U 1 1 62019DEC
P 6500 3400
F 0 "J6" H 6550 4317 50  0000 C CNN
F 1 "Arduino-left" H 6550 4226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x15_P2.54mm_Vertical" H 6500 3400 50  0001 C CNN
F 3 "~" H 6500 3400 50  0001 C CNN
	1    6500 3400
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x15_Odd_Even J7
U 1 1 6203836E
P 7000 3400
F 0 "J7" H 7050 4317 50  0000 C CNN
F 1 "Arduino-left" H 7050 4226 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x15_P2.54mm_Vertical" H 7000 3400 50  0001 C CNN
F 3 "~" H 7000 3400 50  0001 C CNN
	1    7000 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 2700 7300 2700
Wire Wire Line
	6300 2800 7300 2800
Wire Wire Line
	6300 2900 7300 2900
Wire Wire Line
	6300 3000 7300 3000
Wire Wire Line
	6300 3100 7300 3100
Wire Wire Line
	6300 3200 7300 3200
Wire Wire Line
	6300 3300 7300 3300
Wire Wire Line
	6300 3400 7300 3400
Wire Wire Line
	6300 3500 7300 3500
Wire Wire Line
	6300 3600 7300 3600
Wire Wire Line
	6300 3700 7300 3700
Wire Wire Line
	6300 3800 7300 3800
Wire Wire Line
	6300 3900 7300 3900
Wire Wire Line
	6300 4000 7300 4000
Wire Wire Line
	6300 4100 7300 4100
$Comp
L Connector_Generic:Conn_02x15_Odd_Even J10
U 1 1 6204A5F5
P 8100 3350
F 0 "J10" H 8150 4267 50  0000 C CNN
F 1 "Arduino-right" H 8150 4176 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x15_P2.54mm_Vertical" H 8100 3350 50  0001 C CNN
F 3 "~" H 8100 3350 50  0001 C CNN
	1    8100 3350
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x15_Odd_Even J11
U 1 1 6204A5FB
P 8600 3350
F 0 "J11" H 8650 4267 50  0000 C CNN
F 1 "Arduino-right" H 8650 4176 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x15_P2.54mm_Vertical" H 8600 3350 50  0001 C CNN
F 3 "~" H 8600 3350 50  0001 C CNN
	1    8600 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	7900 2650 8900 2650
Wire Wire Line
	7900 2750 8900 2750
Wire Wire Line
	7900 2850 8900 2850
Wire Wire Line
	7900 2950 8900 2950
Wire Wire Line
	7900 3050 8900 3050
Wire Wire Line
	7900 3150 8900 3150
Wire Wire Line
	7900 3250 8900 3250
Wire Wire Line
	7900 3350 8900 3350
Wire Wire Line
	7900 3450 8900 3450
Wire Wire Line
	7900 3550 8900 3550
Wire Wire Line
	7900 3650 8900 3650
Wire Wire Line
	7900 3750 8900 3750
Wire Wire Line
	7900 3850 8900 3850
Wire Wire Line
	7900 3950 8900 3950
Wire Wire Line
	7900 4050 8900 4050
Text Label 5400 1300 2    50   ~ 0
3v3
Text Label 5400 1600 2    50   ~ 0
5v2
Text Label 5400 2100 2    50   ~ 0
gnd2
Text Label 5400 1800 2    50   ~ 0
gnd
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
Text Notes 5150 1900 2    50   ~ 0
4
Text Notes 4800 2000 0    50   ~ 0
gpio 14
Text Notes 5100 2200 2    50   ~ 0
gpio 15
Text Label 5900 1300 0    50   ~ 0
3v3
Text Label 5900 1600 0    50   ~ 0
5v2
Text Label 5900 2100 0    50   ~ 0
gnd2
Text Label 5900 1800 0    50   ~ 0
gnd
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
Text Notes 6150 1900 0    50   ~ 0
4
Text Notes 6500 2000 2    50   ~ 0
gpio 14
Text Notes 6200 2200 0    50   ~ 0
gpio 15
Text Label 5400 1400 2    50   ~ 0
5v
Text Label 5900 1400 0    50   ~ 0
5v
Text Label 8050 1600 0    50   ~ 0
3v3_2
Text Label 8050 1900 0    50   ~ 0
gnd3
Text Label 8050 1300 0    50   ~ 0
gnd4
Text Label 8050 1400 0    50   ~ 0
mosi
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
Text Notes 8350 2000 0    50   ~ 0
27
Text Notes 8300 1800 0    50   ~ 0
22
Text Notes 8400 2200 0    50   ~ 0
gpio 17
Text Notes 8600 2100 2    50   ~ 0
pwm
Text Notes 8400 1700 2    50   ~ 0
23
Text Notes 8400 1500 2    50   ~ 0
24
Text Notes 8550 1400 2    50   ~ 0
gpio 10
Text Label 7550 1600 2    50   ~ 0
3v3_2
Text Label 7550 1900 2    50   ~ 0
gnd3
Text Label 7550 1300 2    50   ~ 0
gnd4
Text Label 7550 1400 2    50   ~ 0
mosi
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
Text Notes 7250 2000 2    50   ~ 0
27
Text Notes 7300 1800 2    50   ~ 0
22
Text Notes 7200 2200 2    50   ~ 0
gpio 17
Text Notes 7000 2100 0    50   ~ 0
pwm
Text Notes 7200 1700 0    50   ~ 0
23
Text Notes 7200 1500 0    50   ~ 0
24
Text Notes 7050 1400 0    50   ~ 0
gpio 10
$Comp
L Connector_Generic:Conn_02x12_Odd_Even J9
U 1 1 61FD1A5A
P 7750 5350
F 0 "J9" H 7800 6067 50  0000 C CNN
F 1 "Conn_02x12_Counter_Clockwise" H 7800 5976 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 7750 5350 50  0001 C CNN
F 3 "~" H 7750 5350 50  0001 C CNN
	1    7750 5350
	1    0    0    -1  
$EndComp
Text Label 8050 5350 0    50   ~ 0
gnd_
Text Label 8050 5850 0    50   ~ 0
gnd_1
Text Label 8050 5250 0    50   ~ 0
sclk2
Text Label 8050 5450 0    50   ~ 0
miso2
Text Label 8050 5650 0    50   ~ 0
spi2_ce2
Text Label 8050 5750 0    50   ~ 0
miso2_pwm
Text Label 8050 5950 0    50   ~ 0
gpio5
Text Label 8050 5550 0    50   ~ 0
gpio10
Text Notes 8350 5950 0    50   ~ 0
13
Text Notes 8500 5950 0    50   ~ 0
pwm
Text Notes 8350 5550 0    50   ~ 0
26
Text Notes 8750 5650 2    50   ~ 0
gpio 16
Text Notes 8650 5450 2    50   ~ 0
gpio 20
Text Notes 8600 5250 2    50   ~ 0
gpio 21
Text Label 8050 5050 0    50   ~ 0
reset
Text Label 8050 4850 0    50   ~ 0
vcc1
Text Label 8050 4950 0    50   ~ 0
vcc
Text Label 8050 5150 0    50   ~ 0
NC
Text Label 7550 5350 2    50   ~ 0
gnd_
Text Label 7550 5850 2    50   ~ 0
gnd_1
Text Label 7550 5250 2    50   ~ 0
sclk2
Text Label 7550 5450 2    50   ~ 0
miso2
Text Label 7550 5650 2    50   ~ 0
spi2_ce2
Text Label 7550 5750 2    50   ~ 0
miso2_pwm
Text Label 7550 5950 2    50   ~ 0
gpio5
Text Label 7550 5550 2    50   ~ 0
gpio10
Text Notes 7250 5950 2    50   ~ 0
13
Text Notes 7100 5950 2    50   ~ 0
pwm
Text Notes 7250 5550 2    50   ~ 0
26
Text Notes 6850 5650 0    50   ~ 0
gpio 16
Text Notes 6950 5450 0    50   ~ 0
gpio 20
Text Notes 7000 5250 0    50   ~ 0
gpio 21
Text Label 7550 5050 2    50   ~ 0
reset
Text Label 7550 4850 2    50   ~ 0
vcc1
Text Label 7550 4950 2    50   ~ 0
vcc
Text Label 7550 5150 2    50   ~ 0
NC
Text Label 9800 5250 2    50   ~ 0
gnd_3
Text Label 9800 5750 2    50   ~ 0
gnd_2
Text Label 9800 5450 2    50   ~ 0
sda
Text Label 9800 5550 2    50   ~ 0
scl
Text Label 9800 5050 2    50   ~ 0
sclk
Text Label 9800 4850 2    50   ~ 0
miso
Text Label 9800 5150 2    50   ~ 0
spi_ce0
Text Label 9800 5350 2    50   ~ 0
spi_ce1
Text Label 9800 5650 2    50   ~ 0
gpio2
Text Label 9800 5850 2    50   ~ 0
gpio3
Text Label 9800 5950 2    50   ~ 0
gpio4
Text Label 9800 4950 2    50   ~ 0
gpio9
Text Notes 9500 5650 2    50   ~ 0
5
Text Notes 9500 5850 2    50   ~ 0
6
Text Notes 9450 4950 0    50   ~ 0
25
Text Notes 9250 5150 0    50   ~ 0
gpio 8
Text Notes 9200 5350 0    50   ~ 0
gpio 7
Text Notes 9400 5550 0    50   ~ 0
gpio 1
Text Notes 9250 5950 0    50   ~ 0
12 pwm
Text Notes 9600 5050 2    50   ~ 0
gpio 11
Text Notes 9600 5450 2    50   ~ 0
gpio 0
Text Notes 9600 4850 2    50   ~ 0
gpio 9
Text Label 10300 5250 0    50   ~ 0
gnd_3
Text Label 10300 5750 0    50   ~ 0
gnd_2
Text Label 10300 5450 0    50   ~ 0
sda
Text Label 10300 5550 0    50   ~ 0
scl
Text Label 10300 5050 0    50   ~ 0
sclk
Text Label 10300 4850 0    50   ~ 0
miso
Text Label 10300 5150 0    50   ~ 0
spi_ce0
Text Label 10300 5350 0    50   ~ 0
spi_ce1
Text Label 10300 5650 0    50   ~ 0
gpio2
Text Label 10300 5850 0    50   ~ 0
gpio3
Text Label 10300 5950 0    50   ~ 0
gpio4
Text Label 10300 4950 0    50   ~ 0
gpio9
Text Notes 10600 5650 0    50   ~ 0
5
Text Notes 10600 5850 0    50   ~ 0
6
Text Notes 10650 4950 2    50   ~ 0
25
Text Notes 10850 5150 2    50   ~ 0
gpio 8
Text Notes 10900 5350 2    50   ~ 0
gpio 7
Text Notes 10700 5550 2    50   ~ 0
gpio 1
Text Notes 10850 5950 2    50   ~ 0
12 pwm
Text Notes 10500 5050 0    50   ~ 0
gpio 11
Text Notes 10500 5450 0    50   ~ 0
gpio 0
Text Notes 10500 4850 0    50   ~ 0
gpio 9
Text Label 4600 4800 0    50   ~ 0
vcc1
$EndSCHEMATC
