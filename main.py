# main.py -- put your code here!
import machine
import neopixel
from neo_pix_matrix_openBit import *
import random
import time
from performance_timer import *
 
led_matrix_MAIN = led_matrix_MAIN()

# 1F1F1F
def led_test():
  led_matrix_MAIN.led_matrix_fill(led_matrix_MAIN.hex_color("000000"))
  led_matrix_MAIN.led_matrix_active()



def main():
  led_test()



















if __name__ == "main":
  pef_timer(main)
