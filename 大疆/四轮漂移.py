import robomaster
from  robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import cv2
# import numpy as np
# print(np.linspace(0,10,1))
ep_robot=robot.Robot()

ep_robot.initialize(conn_type='ap')
ep_robot.led.set_led(comp='all',r=80,g=199,b=190,effect=led.EFFECT_BREATH)

# # ep_robot.chassis.move(x=0.9,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.9,y=0,z=-88,xy_speed=1,z_speed=30).wait_for_completed() #ok
# # ep_robot.chassis.move(x=0.3,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.3,y=0,z=88,xy_speed=1,z_speed=30).wait_for_completed()  #ok
# # ep_robot.chassis.move(x=0.4,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.4,y=0,z=88,xy_speed=1,z_speed=30).wait_for_completed()  #ok
# # ep_robot.chassis.move(x=0.3,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.3,y=0,z=-88,xy_speed=1,z_speed=30).wait_for_completed() #ok
# # ep_robot.chassis.move(x=0.6,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.6,y=0,z=88,xy_speed=1,z_speed=30).wait_for_completed()  #ok
# # ep_robot.chassis.move(x=0.3,y=0,z=0,xy_speed=0.5,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.3,y=0,z=-88,xy_speed=10,z_speed=30).wait_for_completed()  #ok
# # ep_robot.chassis.move(x=0.6,y=0,z=0,xy_speed=0.5,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.5,y=0,z=-88,xy_speed=1,z_speed=30).wait_for_completed()   #ok
# # ep_robot.chassis.move(x=0.3,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.3,y=0,z=88,xy_speed=1,z_speed=30).wait_for_completed()    #ok
# # ep_robot.chassis.move(x=0.3,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0.2,y=0,z=88,xy_speed=1,z_speed=30).wait_for_completed()    #ok
ep_robot.chassis.move(x=0.2,y=0,z=0,xy_speed=1,z_speed=30).wait_for_completed()       #ok
ep_robot.chassis.move(x=0,y=1,z=88,xy_speed=1,z_speed=30).wait_for_completed()        #ok
# # ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=1,z_speed=30).wait_for_completed()
ep_robot.close()
