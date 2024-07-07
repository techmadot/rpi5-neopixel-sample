import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 25
PIXEL_ORDER = neopixel.GRB
COLORS = (0xFF0000, 0x00FF00, 0x0000FF)
DELAY = 0.02

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False
)

class RGBW(int):
    def __new__(self, r, g=None, b=None, w=None):
        if (g,b,w) == (None, None, None):
            return int.__new__(self, r)
        else:
            if w is None:
                w = 0
            return int.__new__(self, (w << 24) | (r << 16) | (g << 8) | b)
    @property
    def r(self):
        return (self >> 16) & 0xFF
    @property
    def g(self):
        return (self >> 8) & 0xFF
    @property
    def b(self):
        return (self) & 0xFF
    @property
    def w(self):
        return (self >> 24) & 0xFF
    
    
def Color(red, green, blue, white=0):
    return RGBW(red, green, blue, white)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.n):
        strip[i] = color
        strip.show()
        time.sleep(wait_ms/ 1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.n, 3):
                if i+q < strip.n:
                    strip[i+q] = color
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.n, 3):
                if i+q < strip.n:
                    strip[i+q] = 0


def wheel(pos):
    if pos < 85:
        return Color(pos*3, 255-pos*3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos*3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.n):
            strip[i] = wheel((int(i * 256 / strip.n) + j) & 255)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(0, 256 * iterations, 4):
        for i in range(strip.n):
            strip[i] = wheel((int(i * 256 / strip.n) + j) & 255)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(0, 256, 2):
        for q in range(3):
            for i in range(0, strip.n, 3):
                if i + q < strip.n:
                    strip[i + q] = wheel((i + j) % 255)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.n, 3):
                if i + q < strip.n:
                    strip[i + q] = 0

if __name__ == '__main__':
    try:
        while True:
            print('Color wipe animations')
            colorWipe(pixels, Color(255, 0, 0))
            colorWipe(pixels, Color(0, 255, 0))
            colorWipe(pixels, Color(0, 0, 255))
            print('Theater chase animation')
            theaterChase(pixels, Color(127, 127, 127)) # White theater chase
            theaterChase(pixels, Color(127, 0, 0)) # Red theater chase
            theaterChase(pixels, Color(0, 0, 127)) # Blue theater chase
            print('Rainbow animations.')
            rainbow(pixels)
            rainbowCycle(pixels)
            theaterChaseRainbow(pixels)


    except KeyboardInterrupt:
        colorWipe(pixels, (0,0,0), 10)
