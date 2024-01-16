# main.py -- put your code here!
import machine
import neopixel
from neo_pix_matrix_openBit import *
import random
import time
from performance_timer import *
import betterESPNOW

 
led_matrix_MAIN = led_matrix_MAIN()
espNow = betterESPNOW.ESPN()



# 1F1F1F

def testUnit():
  led_matrix_MAIN.led_matrix_fill(led_matrix_MAIN.hex_color("000000"))
  led_matrix_MAIN.led_matrix_active()
  time.sleep(2)
  led_matrix_MAIN.led_matrix_fill(led_matrix_MAIN.hex_color("001F1F"))
  led_matrix_MAIN.led_matrix_active()
  print(espNow.getMyMAC()) # 10:97:BD:25:35:80
  
  
  espNow.addPeer('E8:31:CD:1E:BC:20', 2)
  
  


def main():
  testUnit()
  espNow._print_peers_info()
    















if __name__ == "main":
  # pef_timer(main)
  main()
