from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
num1 = randint(1,56)
num2 = randint(1,56)
num3 = randint(1,56)
num4 = randint(1,56)


while True:
    # sense.show_message("IIII", text_colour=blue, back_colour=red, scroll_speed=0.001)
    print("Dagens tal er:" + str(num1) + " , " + str(num2) + " , " + str(num3) + " , " + str(num4))

    sense.show_message("tallene er:", scroll_speed=0.02)

    sleep(2.0)
    sense.show_message(str(num1), text_colour=red, back_colour=blue)
    sleep(2.0)
    sense.show_message(str(num2), text_colour=red)
    sleep(2.0)
    sense.show_message(str(num3), text_colour=red)
    sleep(2.0)
    sense.show_message(str(num4), text_colour=red)


    
    print("Data:")
    pressure = sense.get_pressure()
    print("Pressure is : " + str(pressure))

    temp = sense.get_temperature()
    print("Temperature is: " + str(temp))
    if temp > 30:
        print("Way too hot")

    humidity = sense.get_humidity()
    print("humidity: " + str(humidity))
    
