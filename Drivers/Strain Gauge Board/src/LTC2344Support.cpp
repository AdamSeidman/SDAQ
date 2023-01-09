#include "LTC2344Support.h"
#include "pico/stdlib.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
#include "pico_driver.h"
#include "hardware/clocks.h"
#include "time.h"
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

void LTC2344_waitinterrupt()
{
    has_interrupt_happened = false;
    while (!has_interrupt_happened)
        ;
}
void LTC2344_readvalues(SoftSpanPacket_t SoftSpan, uint8_t ReadVals[12])
{
    gpio_put(CNV, true);
    LTC2344_waitinterrupt();
    gpio_put(CNV, false);
    uint8_t write_vals[12] = {0};
    write_vals[10] = (uint8_t)SoftSpan.SS3;
    write_vals[11] = 
}
}  // namespace sixteen_bits
}  // namespace LTC2344