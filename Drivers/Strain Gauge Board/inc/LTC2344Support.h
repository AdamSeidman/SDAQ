#pragma once
#include <stdint.h>
#define NUM_BITS 16
namespace LTC2344
{
namespace sixteen_bits
{
struct ReturnPacket_t
{
    union
    {
        uint8_t val_list[4];
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
struct SoftSpanPacket_t
{
    union
    {
        uint16_t vals;
        struct
        {
            uint16_t ZERO : 4;
            uint16_t SS3 : 3;
            uint16_t SS2 : 3;
            uint16_t SS1 : 3;
            uint16_t SS0 : 3;
        };
    };
};
enum SoftSpanConfig
{
    FULLRANGE = 0b111,
    FULLRANGE_OVER1024 = 0b110,
    ZERO_TO_FULL = 0b101,
    ZERO_TO_FULL_OVER1024 = 0b100,
    HALFRANGE = 0b011,
    HALFRANGE_OVER1024 = 0b010,
    ZERO_TO_HALFRANGE = 0b001,
    OFF = 0b000
};
void LTC2344_readvalues(SoftSpanPacket_t SoftSpanConfig, uint8_t returnPacket[12]);
inline static SoftSpanPacket_t LTC2344_CreateSSPacket(SoftSpanConfig SS0, SoftSpanConfig SS1, SoftSpanConfig SS2,
                                                      SoftSpanConfig SS3)
{
    SoftSpanPacket_t packet = {0};
    packet.SS0 = SS0;
    packet.SS1 = SS1;
    packet.SS2 = SS2;
    packet.SS3 = SS3;
    return packet;
}
}  // namespace sixteen_bits
}  // namespace LTC2344