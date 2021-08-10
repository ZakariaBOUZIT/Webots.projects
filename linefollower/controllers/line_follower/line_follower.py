"""line_follower controller."""
from controller import Robot

robot = Robot()
time_step = 32
max_speed = 6.28/2
#motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
#ir sensors
left_ir = robot.getDevice('ir0')
left_ir.enable(time_step)
right_ir = robot.getDevice('ir1')
right_ir.enable(time_step)
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


# Main loop:
while robot.step(timestep) != -1:
     #read ir sensors
     left_ir_value = left_ir.getValue()
     right_ir_value = right_ir.getValue()
     print("left : {} , right : {}".format(left_ir_value,right_ir_value))
     
     left_speed = max_speed*0.75
     right_speed = max_speed*0.75
     
     if (left_ir_value > right_ir_value) and (6 < left_ir_value < 15):
        print("go left")
        left_speed = -max_speed*0.75
     elif (right_ir_value > left_ir_value) and (6 < right_ir_value < 15): 
        print("go right")
        right_speed = -max_speed*0.75
     
     left_motor.setVelocity(left_speed)
     right_motor.setVelocity(right_speed)
