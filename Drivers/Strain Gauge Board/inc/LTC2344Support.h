#pragma once
#include <stdint.h>
#define NUM_BITS 16
struct LTC2344Packet_t
{
    union
    {
        uint32_t total_val;
        struct
        {
            uint8_t null_val;
            uint16_t ADC_val;
            union
            {
                uint8_t val;
                struct
                {
                    uint8_t zeros : 3;
                    uint8_t chan_id : 2;
                    uint8_t SoftSpan : 3;
                };
            };
        };
    };
};