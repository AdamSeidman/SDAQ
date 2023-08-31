#include "pico.h"
#include <stdio.h>
#include "hardware/spi.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
#include "hardware/i2c.h"
#include "hardware/regs/clocks.h"
#include "hardware/platform_defs.h"
#include "hardware/clocks.h"
#include "hardware/watchdog.h"
#include "hardware/pll.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
#include "pico_driver.h"
#include <pico/stdlib.h>
#include <pico/i2c_slave.h>
#include <pico/binary_info/code.h>
#include <pico/mutex.h>
#include <pico/lock_core.h>
#include <stdlib.h>
#include <algorithm>
#include <iterator>
struct NoInitTag
{
};
uint8_t get_i2c_addr()
{
    // Same stupid al-gore-rythm as the ADC board
    int id = (gpio_get(8) << 2) + gpio_get(9) + gpio_get(10) + gpio_get(11);

    return STRAIN_BOARD | id;
}
struct __attribute__((packed)) spi_output_adc
{
    uint32_t adc0 : 24;
    uint32_t adc1 : 24;
    uint32_t adc2 : 24;
    uint32_t adc3 : 24;
};
template <typename T>
class mutex_locker
{
    mutex_locker(T) = delete;
};
template <>
class mutex_locker<mutex_t>
{
  public:
    mutex_locker(mutex_t mut) { mutex_enter_blocking(&mut); }
    ~mutex_locker() { mutex_exit(&mut); }

  private:
    mutex_t mut;
};
struct adc_output_gated
{
  public:
    adc_output_gated(NoInitTag) {}
    adc_output_gated() { mutex_init(&mut); }
    void set_output(spi_output_adc adc_out)
    {
        mutex_locker<mutex_t> locker(mut);
        adc_output = adc_out;
    }
    spi_output_adc get_output()
    {
        mutex_locker<mutex_t> locker(mut);
        return adc_output;
    }

  private:
    mutex_t mut;
    spi_output_adc adc_output;
};
adc_output_gated gated_adc(NoInitTag{});
int core1_main()
{
    gpio_set_input_enabled(16, true);
    gpio_set_irq_enabled_with_callback(16, GPIO_IRQ_EDGE_RISE, true, [](uint gpio, uint32_t events) {
        spi_output_adc adc_output = {};
        spi_read_blocking(spi0, 0, (uint8_t*)&adc_output, sizeof(spi_output_adc));
        gated_adc.set_output(adc_output);
    });
    return 0;
}
int main()
{
    gated_adc = adc_output_gated();
    gpio_init_mask(1 << 8 | 1 << 9 | 1 << 10 | 1 << 11);
    gpio_set_input_enabled(8, true);
    gpio_set_input_enabled(9, true);
    gpio_set_input_enabled(10, true);
    gpio_set_input_enabled(11, true);
    constexpr int MHz = 1'000'000;
    // We want *maximally* 27Mhz, spi_init will always round down to be below this if the division from whatever value our clock
    // frequency is isn't clean, or throw an error.
    bi_decl(bi_3pins_with_func(PICO_DEFAULT_SPI_RX_PIN, PICO_DEFAULT_SPI_TX_PIN, PICO_DEFAULT_SPI_SCK_PIN, GPIO_FUNC_SPI));
    spi_init(spi0, 27 * MHz);
    i2c_init(i2c0, I2C_RATE);
    bi_decl(bi_2pins_with_func(PICO_DEFAULT_I2C_SCL_PIN, PICO_DEFAULT_I2C_SDA_PIN, GPIO_FUNC_I2C));
    i2c_set_slave_mode(i2c0, true, get_i2c_addr());

    uint8_t zeros[4] = {0};
    uint8_t vals[24 * 4] = {0};
    while (true)
    {
        uint8_t request = 0;
        i2c_read_raw_blocking(i2c0, &request, 1);
        enum request_types
        {
            RETURN_FORMAT = 1,
            DEFAULT = 0,
        };
        switch (request)
        {
            case RETURN_FORMAT:
            // I haven't decided how this protocol will work, for now default to the same as the ADC board
            default: {
                spi_read_blocking(spi0, 0x00, vals, 24 * 4);
                i2c_write_raw_blocking(i2c0, zeros, 4);
            }
            break;
        }
    }
}