# main.py -- put your code here!
import machine
import neopixel
from neo_pix_matrix_openBit import *
import random
import time
from performance_timer import *

led_matrix = led_matrix()


def led_test():
    led_matrix.led_matrix_fill((random.randint(16,255),random.randint(16,255),random.randint(16,255)))
    led_matrix.led_matrix_active()



def main():
    for _ in range(500):
        led_test()
    
    
    
    
pef_timer(main()) 
