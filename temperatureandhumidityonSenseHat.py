from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
temp = sense.get_temperature()
humidity = sense.get_humidity()



while True:
    print("Temperaturen er: {:.2f}C".format(temp))
    print("Humidity er: {:.2f}".format(humidity))
    
    if temp > 20 and humidity > 20:
        print("Open a window!")
    if temp > 30:
        print("Way too hot")
        sense.show_message("Open a window!")
 
    sense.show_message("{:.2f}C".format(temp))
    sleep(2.0)
    sense.show_message("{:.2f}Humidity".format(humidity))

    
  