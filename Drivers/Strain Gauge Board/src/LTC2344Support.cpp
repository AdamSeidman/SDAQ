#include "LTC2344Support.h"
#include "pico/stdlib.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
#include "pico_driver.h"
#include "hardware/clocks.h"
#include "time.h"
#include "hardware/spi.h"
namespace LTC2344
{
namespace sixteen_bits
{
volatile bool has_interrupt_happened;
void LTC2344_inform_happened(uint gpio, uint32_t events) { has_interrupt_happened = true; }
void LTC2344_setup()
{
    gpio_set_dir(CNV, true);
    gpio_set_dir(BUSY, false);
    gpio_pull_down(CNV);
    gpio_set_irq_enabled_with_callback(BUSY, GPIO_IRQ_EDGE_FALL, true, LTC2344_inform_happened);
}

void LTC2344_sendcnv()
{
    has_interrupt_happened = false;
    gpio_put(CNV, true);
    while (!has_interrupt_happened)
        ;
    gpio_put(CNV, false);
}
void LTC2344_readvalues(SoftSpanPacket_t SoftSpan, uint8_t ReadVals[12])
{
    LTC2344_sendcnv();
    uint8_t write_vals[12] = {0};
    write_vals[10] = (SoftSpan.vals & 0xFF00) >> 8;
    write_vals[11] = SoftSpan.vals & 0xFF;
    spi_write_read_blocking(spi0, write_vals, ReadVals, sizeof(uint8_t) * 12);
}
}  // namespace sixteen_bits
}  // namespace LTC2344