"""drive_my_bot controller.
differential bot odometry using encoders.
"""
from controller import Robot
import math

robot = Robot()
timestep = 64
max_speed = 6.28
ps_values=[0,0]
last_ps_values=[0,0]
dist_values=[0,0]
robot_pose = [0, 0, 0] #x,y,teta

# create instance of motors
left_motor = robot.getMotor('motor1')
right_motor = robot.getMotor('motor2')
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)
# create instance of encoders
left_ps = robot.getPositionSensor('ps1')
left_ps.enable(timestep)
right_ps = robot.getPositionSensor('ps2')
right_ps.enable(timestep)
#compute encoder unit
wheel_radius = 0.025
distance_between_wheels = 0.09
encoder_unit = (2 * 3.14 * wheel_radius)/6.28

# Main loop:
while robot.step(timestep) != -1:
    #read odometry     
    ps_values[0] = left_ps.getValue()
    ps_values[1] = right_ps.getValue()
    #convertion
    for i in range(2):
        diff = ps_values[i] - last_ps_values[i]
        if diff < 0.001:
           diff = 0
           ps_values[i] = last_ps_values[i]
        
        dist_values[i] = diff * encoder_unit
    #linear and angular velocity
    v = (dist_values[0] + dist_values[1])/2.0
    w = (dist_values[0] - dist_values[1])/distance_between_wheels
    
    dt = 1
    robot_pose[2] +=  w*dt
    
    vx = v*math.cos(robot_pose[2])
    vy = v*math.sin(robot_pose[2]) 
    
    robot_pose[0] += vx*dt
    robot_pose[1] += vy*dt
    
    print('robot pose:{}'.format(robot_pose))
              
    left_motor.setVelocity(max_speed/2)
    right_motor.setVelocity(max_speed)
    
    last_ps_values[i] = ps_values[i]