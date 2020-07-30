"""rovio controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

TIME_STEP = 64

# create the Robot instance.
robot = Robot()

# get the wheels
wheels = []
wheelNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for name in wheelNames:
    motor = robot.getMotor(name)
    motor.setPosition(float('inf'))
    motor.setVelocity(-1.5)
    wheels.append(motor)

ds = []
dsNames = ['ds_left', 'ds_right']
for name in dsNames:
    sensor = robot.getDistanceSensor(name)
    sensor.enable(TIME_STEP)
    ds.append(sensor)

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
def goForward():
    for motor in wheels:
        motor.setVelocity(-3)
        
def goRight():
    for i in range(4):
        motor = wheels[i]
        if i % 2:
            motor.setVelocity(3)
        else:
            motor.setVelocity(-3)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    for sensor in ds:
        if sensor.getValue() < 1000:
            goRight()
            break;
        else:
            goForward()
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
