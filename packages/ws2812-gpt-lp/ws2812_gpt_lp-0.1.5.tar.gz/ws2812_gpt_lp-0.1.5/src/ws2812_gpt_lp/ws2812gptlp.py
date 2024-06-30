import spidev
import time

class WS2812:
    def __init__(self, spi_bus, spi_device, num_leds):
        """Initialise la configuration SPI et le nombre de LEDs."""
        if num_leds <= 0:
            raise ValueError("Number of LEDs must be greater than 0")
        
        self.spi_bus = spi_bus
        self.spi_device = spi_device
        self.num_leds = num_leds
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 4000000  # 4 MHz, ajustez si nécessaire
        self.leds = [(0, 0, 0)] * num_leds  # Initialiser toutes les LEDs à éteint

        # Envoyer une séquence de reset initiale pour s'assurer que les LEDs sont bien réinitialisées
        self.spi.xfer2([0] * 100)
        time.sleep(0.01)

    def encode_byte(self, byte):
        """Encode un octet en séquence de bits pour WS2812 via SPI."""
        encoded = []
        for i in range(8):
            if byte & (1 << (7 - i)):
                encoded.append(0b11100000)  # Bit 1
            else:
                encoded.append(0b10000000)  # Bit 0
        return encoded

    def encode_color(self, r, g, b):
        """Encode une couleur RGB en séquence de bits pour WS2812 via SPI."""
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be between 0 and 255")
        
        data = []
        data += self.encode_byte(g)  # WS2812 attend l'ordre GRB
        data += self.encode_byte(r)
        data += self.encode_byte(b)
        return data

    def send_colors(self, colors):
        """Envoie une liste de couleurs RGB aux LEDs WS2812."""
        if len(colors) != self.num_leds:
            raise ValueError(f"Number of colors ({len(colors)}) must match number of LEDs ({self.num_leds})")
        
        self.leds = colors  # Mettre à jour la liste interne de LEDs
        data = []
        for r, g, b in colors:
            data += self.encode_color(r, g, b)
        self.spi.xfer2(data)
        time.sleep(0.001)  # Petite pause pour permettre la stabilisation
        self.spi.xfer2([0] * 50)  # Séquence de reset plus longue

    def send_color(self, led_index, r, g, b):
        """Change la couleur d'une LED en particulier."""
        if not (0 <= led_index < self.num_leds):
            raise ValueError(f"LED index must be between 0 and {self.num_leds - 1}")
        
        self.leds[led_index] = (r, g, b)  # Mettre à jour la couleur de la LED
        self.send_colors(self.leds)  # Envoyer la mise à jour à toutes les LEDs

    def send_off(self):
        """Éteint toutes les LEDs."""
        self.send_colors([(0, 0, 0)] * self.num_leds)

    def send_to_all(self, r, g, b):
        """Envoie la même couleur à toutes les LEDs."""
        self.send_colors([(r, g, b)] * self.num_leds)

    def close(self):
        """Termine la connexion SPI."""
        self.spi.close()

# Exemple d'utilisation
if __name__ == "__main__":
    num_leds = 8
    ws2812 = WS2812(spi_bus=4, spi_device=0, num_leds=num_leds)

    # Définir les couleurs pour 8 LEDs
    colors = [
        (255, 0, 0),  # Rouge
        (0, 255, 0),  # Vert
        (0, 0, 255),  # Bleu
        (255, 255, 0),  # Jaune
        (0, 255, 255),  # Cyan
        (255, 0, 255),  # Magenta
        (255, 255, 255),  # Blanc
        (0, 0, 0)     # Noir (éteint)
    ]

    # Envoyer les couleurs aux LEDs
    ws2812.send_colors(colors)
    time.sleep(5)

    # Changer la couleur de la première LED à bleu
    ws2812.send_color(0, 0, 0, 255)
    time.sleep(5)

    # Éteindre toutes les LEDs
    ws2812.send_off()
    time.sleep(1)

    # Envoyer la couleur rouge à toutes les LEDs
    ws2812.send_to_all(255, 0, 0)
    time.sleep(5)

    # Éteindre toutes les LEDs
    ws2812.send_off()

    # Terminer la connexion SPI
    ws2812.close()
