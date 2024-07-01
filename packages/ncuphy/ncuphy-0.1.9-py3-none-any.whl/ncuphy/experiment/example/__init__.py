__list__ = ['StepperMotor', "ADS1115", "MPU9250", "MPU6050"]

__which__ = input(f"Which module do you want to import? \n{__list__}\nEnter the module name:")

assert __which__ in __list__, f"Module {__which__} not found in {__list__}"


__stepper_motor_example = """
from ncuphy.experiment import StepperMotor

# display logging, not necessary ---------------------------------------------

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# -----------------------------------------------------------------------------

# define the pins
pul = 26
dir = 19
ena = 13

# define the delay between pulses
pulse_delay = 0.001

# create the stepper motor object
motor = StepperMotor(pul, dir, ena, pulse_delay)

# move the stepper motor by 1000 steps
motor.step(1000)

# move the stepper motor in the other direction by 1500 steps
motor.step(-1500)

# get the current position of the stepper motor
position = motor.position
print(f"Current position: {position}")

# move the stepper motor to the home position
motor.home()

# move the stepper motor again by 100 steps
motor.step(100)

# get the current position of the stepper motor
position = motor.position
print(f"Current position: {position}")

# set the current position as the home position
motor.sethome()

# move the stepper motor by 500 steps
position = motor.position
print(f"Current position: {position}")
"""


if __which__ == "StepperMotor":
    with open('.Example_StepperMotor.py', 'w') as f:
        f.write(__stepper_motor_example)