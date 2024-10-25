"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *


import random

# Copyright (c) 2020 MTHS All rights reserved
# Created by: Mr. Coxall
# Created on: Sep 2020
# This program generates random numbers and compares

random_number1 = None
random_number2 = None

def clear_screen():
    print("\033[H\033[J")  # Clear the console screen

def show_icon(icon_name):
    print(f"[{icon_name}]")  # Placeholder for showing an icon

def show_string(message):
    print(message)  # Display the message

# #1 number
def on_button_a():
    global random_number1
    random_number1 = random.randint(0, 99)
    clear_screen()
    show_string(f'# 1: {random_number1}')
    show_icon("Happy")

# #2 number
def on_button_b():
    global random_number2
    random_number2 = random.randint(0, 99)
    clear_screen()
    show_string(f'# 2: {random_number2}')
    show_icon("Happy")

# shake
def on_shake():
    clear_screen()
    if random_number1 > random_number2:
        show_string(f'{random_number1} > {random_number2}')
    elif random_number1 < random_number2:
        show_string(f'{random_number1} < {random_number2}')
    else:
        show_string(f'{random_number1} = {random_number2}')
    show_icon("Happy")

# Simulate button presses and shake
on_button_a()  # Simulating Button A pressed
on_button_b()  # Simulating Button B pressed
on_shake()     # Simulating a shake gesture
