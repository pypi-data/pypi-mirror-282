# WS2812-GPT-LP

This library allows you to control WS2812 LEDs using SPI on Orange Pi.
Cette bibliothèque permet de contrôler les LEDs WS2812 via SPI sur Orange Pi.

## Installation

pip install ws2812-gpt-lp

## Usage

from ws2812_gpt_lp import WS2812

# Configuration
num_leds = 8
ws2812 = WS2812(spi_bus=4, spi_device=0, num_leds=num_leds)

# Set colors for 8 LEDs
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 255),  # White
    (0, 0, 0)     # Black (off)
]

# Send colors to LEDs
ws2812.send_colors(colors)

# Change the color of the first LED to blue
ws2812.send_color(0, 0, 0, 255)

# Turn off all LEDs
ws2812.send_off()

# Set all LEDs to red
ws2812.send_to_all(255, 0, 0)

# Close the SPI connection
ws2812.close()

## Note

You must solder a 100nF capacitor between the VCC and GND of the WS2812 LEDs to avoid interference.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

This library was jointly developed by Laurent Pastor and ChatGPT 4.
