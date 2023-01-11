#include "LTC2344Support.h"
#include "pico.h"
#include <stdio.h>
#include "hardware/spi.h"
#include "hardware/irq.h"
#include "hardware/gpio.h"
#include "hardware/i2c.h"
#include "pico_driver.h"
#include <stdlib.h>
#include <algorithm>
#include <iterator>
uint8_t get_i2c_addr()
{
    int id = (gpio_get(8) << 2) + gpio_get(9) + gpio_get(10) + gpio_get(11);

    return STRAIN_BOARD | id;
}
int main()
{
    using namespace LTC2344::sixteen_bits;
    gpio_init_mask(1 << 8 | 1 << 9 | 1 << 10 | 1 << 11);
    gpio_set_input_enabled(8, true);
    gpio_set_input_enabled(9, true);
    gpio_set_input_enabled(10, true);
    gpio_set_input_enabled(11, true);
    // LTC2344 docs, page 33, 100kS/s = 13Mhz with 1 SDO lane
    spi_init(spi0, 13 * 1000000);
    i2c_init(i2c0, I2C_RATE);
    i2c_set_slave_mode(i2c0, true, get_i2c_addr());
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
                uint8_t ReadVals[12];
                LTC2344_readvalues(LTC2344_CreateSSPacket(SoftSpanConfig::HALFRANGE, SoftSpanConfig::HALFRANGE,
                                                          SoftSpanConfig::HALFRANGE, SoftSpanConfig::HALFRANGE),
                                   ReadVals);
                ReturnPacket_t packets[4];
                uint8_t countdown = 12;
                // Four packets of 3 values, part of this look could theoretically be unrolled into a STRH and a STRB but honestly
                // I'm a lazy bastard, let the compiler optimize my code here
                for (int j = 0; j < 4; j++)
                {
                    for (int i = 0; i < 3; i++)
                    {
                        // Multi-value reading can theoretically stretch this into a few vector instructions as well, but because
                        // this is a cortex-m0+ no such speedup operation should exist here other than the one mentioned above An
                        // extra 3 instructions that take up a couple hundred ns is not an issue when we already did most of the
                        // time-sensitive work
#define ReadValIntoPacket(packet, packetNum, readingval, counter) \
    packet[packetNum].val_list[3 - i] = readingval[counter];      \
    counter--
                        ReadValIntoPacket(packets, i, ReadVals, countdown);
                    }
                }
                std::sort(std::begin(packets), std::end(packets),
                          [](ReturnPacket_t a, ReturnPacket_t b) { return a.chan_id < b.chan_id; });

                for (auto packet : packets)
                {
                    uint16_t adc_val = packet.ADC_val;
                    uint8_t adc_firstpacket[2] = {(uint8_t)(adc_val & 0xFF), (uint8_t)((adc_val >> 8) & 0xFF)};
                    i2c_write_raw_blocking(i2c0, adc_firstpacket, 2);
                }
                uint8_t zeros[4] = {0};
                i2c_write_raw_blocking(i2c0, zeros, 4);
            }
            break;
        }
    }
}