from sense_hat import SenseHat
import time

sense = SenseHat()

RED = (255, 0, 0)
BLUE = (0, 0, 255)

def police_siren():
    try:
        while True:
            sense.clear(RED)
            time.sleep(0.5)
            sense.clear(BLUE)
            time.sleep(0.5)
    except KeyboardInterrupt:
        sense.clear()

if __name__ == "__main__":
    police_siren()
