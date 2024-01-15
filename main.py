# main.py -- put your code here!
import machine
import neopixel
from neo_pix_matrix_openBit import *
import random
import time
from performance_timer import *
import betterESPNOW
import espnow

 
led_matrix_MAIN = led_matrix_MAIN()
espNow = betterESPNOW.ESPN()



# 1F1F1F

def testUnit():
  led_matrix_MAIN.led_matrix_fill(led_matrix_MAIN.hex_color("000000"))
  led_matrix_MAIN.led_matrix_active()
  time.sleep(2)
  led_matrix_MAIN.led_matrix_fill(led_matrix_MAIN.hex_color("1F1F1F"))
  led_matrix_MAIN.led_matrix_active()
  
  espNow.addPeer('ff:ff:ff:ff:ff:ff')
  while True:
    time.sleep(1)
    espNow.send("hello", "ff:ff:ff:ff:ff:ff")


def main():
  testUnit()
















if __name__ == "main":
  # pef_timer(main)
  main()
