#region VEXcode Generated Robot Configuration


#THIS CODE IF YOU WANT TO USE IT, MUST BE DOWNLOADED TO A V5 VEX BRAIN THROUGH VEXCODE V5

from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# vex-vision-config:begin
vision1__TOP__BACK = Signature(1, 993, 2083, 1538,-2821, -1855, -2338,2.5, 0)
vision1__TOP_FRONT = Signature(2, 0, 0, 0,0, 0, 0,3, 0)
vision1__UNDER_FRONT = Signature(3, 1103, 1999, 1551,-2575, -1961, -2268,2.5, 0)
vision1 = Vision(Ports.PORT9, 50, vision1__TOP__BACK, vision1__TOP_FRONT, vision1__UNDER_FRONT)
# vex-vision-config:end
wall = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
door = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

vexcode_vision1_objects = []
myVariable = 0
cane1 = Event()
cane2 = Event()

def when_started1():
    global myVariable, message1, cane, cane1, cane2, cane3, vexcode_vision1_objects
    wall.set_stopping(BRAKE)
    door.set_stopping(HOLD)
    door.set_velocity(100, PERCENT)
    wall.set_velocity(100, PERCENT)
    while True:
        cane1.broadcast_and_wait()
        cane2.broadcast_and_wait()
        wait(0.1, SECONDS)
        wait(5, MSEC)

def cane1_callback_0():
    global myVariable, message1, cane, cane1, cane2, cane3, vexcode_vision1_objects
    vexcode_vision1_objects = vision1.take_snapshot(vision1__TOP__BACK)
    if vexcode_vision1_objects and len(vexcode_vision1_objects) > 0:
        door.spin_to_position(180, DEGREES)
        for repeat_count in range(9):
            wall.spin_for(REVERSE, 336, DEGREES)
            wait(0.1, SECONDS)
            wall.spin_for(FORWARD, 168, DEGREES)
            wait(0.1, SECONDS)
            wait(5, MSEC)
        wait(2, SECONDS)
        wall.spin_for(REVERSE, 185, DEGREES)
        wait(2, SECONDS)
        for repeat_count2 in range(10):
            wall.spin_for(FORWARD, 100, DEGREES)
            wall.spin_for(REVERSE, 100, DEGREES)
            wait(5, MSEC)
        door.spin_to_position(0, DEGREES)
        wait(5, SECONDS)
        wall.spin_for(FORWARD, 1696, DEGREES)

def cane2_callback_0():
    global myVariable, message1, cane, cane1, cane2, cane3, vexcode_vision1_objects
    vexcode_vision1_objects = vision1.take_snapshot(vision1__UNDER_FRONT)
    if vexcode_vision1_objects and len(vexcode_vision1_objects) > 0:
        door.spin_to_position(180, DEGREES)
        for repeat_count3 in range(9):
            wall.spin_for(REVERSE, 336, DEGREES)
            wait(0.1, SECONDS)
            wall.spin_for(FORWARD, 168, DEGREES)
            wait(0.1, SECONDS)
            wait(5, MSEC)
        wait(2, SECONDS)
        wall.spin_for(REVERSE, 185, DEGREES)
        wait(2, SECONDS)
        for repeat_count4 in range(10):
            wall.spin_for(FORWARD, 100, DEGREES)
            wall.spin_for(REVERSE, 100, DEGREES)
            wait(5, MSEC)
        door.spin_to_position(0, DEGREES)
        wait(5, SECONDS)
        wall.spin_for(FORWARD, 1696, DEGREES)

# system event handlers
cane1(cane1_callback_0)
cane2(cane2_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
