#include "LTC2344Support.h"
#include "pico.h"
#include <stdio.h>
#include "hardware/spi.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"

int main()
{
    // LTC2344 docs, page 33, 1kS/s = 13Mhz with 1 SDO lane
    spi_init(spi0, 13 * 1000000);
    
}