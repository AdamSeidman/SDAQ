#include "LTC2344Support.h"
#include "pico.h"
#include "hardware/spi.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
int main()
{
    spi_init(spi0, 480000);
}