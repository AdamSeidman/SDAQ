#include "LTC2344Support.h"
#include "pico.h"
#include "hardware/spi.h"
int main()
{
    spi_init(spi0, 480000);
}