import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import cv2
# import numpy as npyx
# print(np.linspace(0,10,1))
ep_robot=robot.Robot()
# robomaster.config.LOCAL_IP_STR = "192.168.0.107"
ep_robot.initialize(conn_type='ap')
ep_robot.led.set_led(comp='all',r=10,g=100,b=100,effect=led.EFFECT_BREATH)

# ep_robot.chassis.drive_speed(x=-0.5,y=0,z=0,timeout=1)
# time.sleep(3)
# ep_robot.chassis.drive_speed(x=0,y=0,z=90,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0.2,y=0,z=0,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0,y=0,z=90,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0.2,y=0,z=0,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0,y=0,z=90,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0.2,y=0,z=0,timeout=2)
# time.sleep(1)
# ep_robot.chassis.drive_speed(x=0,y=0,z=90,timeout=2)
# time.sleep(1)
# ep_robot.chassis.move(x=-1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
# ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=1).wait_for_completed()
#
# ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=0.5,z_speed=0).wait_for_completed()
# ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=1).wait_for_completed()

###
# def speed(r,w):
#     w_1 = w + (10)*w/r
#     w_2 = w - (10)*w/r
#     return [int(w_1),int(w_2)]
# # r = int(input("请输入走圆周运动的半径："))
# # w = int(input("请输入机器人的速度："))
# r=20
# w=20
# v = speed(r,w)
# print(v)
#
# ep_robot.chassis.drive_wheels(w1=0, w2=190, w3=600,w4=400)
# time.sleep(0.6)
# ep_robot.chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
# time.sleep(0.5)
#
# ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=5).wait_for_completed()
# time.sleep(0.5)
####
# ep_robot.chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
# time.sleep(10)
# for i in range(18):
#     ep_robot.chassis.move(x=0.1,y=0,z=0,xy_speed=5).wait_for_completed()
#     ep_robot.chassis.move(x=0, y=0, z=20, z_speed=60).wait_for_completed()
    # ep_robot.chassis.drive_speed(x=0.2, y=0, z=0, timeout=2)
    # time.sleep(1)
    # ep_robot.chassis.drive_speed(x=0, y=0, z=90, timeout=2)
    # time.sleep(1)
    # ep_robot.chassis.move(x=0.7, y=0, z=0, xy_speed=0.5, z_speed=0).wait_for_completed()
    # ep_robot.chassis.move(x=0, y=0, z=90, xy_speed=0, z_speed=1).wait_for_completed()

    # ep_robot.chassis.move(x=1, y=0, z=0, xy_speed=0.5, z_speed=0).wait_for_completed()
    # ep_robot.chassis.move(x=0, y=0, z=90, xy_speed=0, z_speed=1).wait_for_completed()


# ep_robot.chassis.move(x=0.7,y=0,z=0,xy_speed=0.5,z_speed=0).wait_for_completed()
# ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=1).wait_for_completed()
#
# ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=0.5,z_speed=0).wait_for_completed()
# ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=1).wait_for_completed()
#

# while True:
#     a = input("请输入方向（w/a/s/d）:")
#     if a == 'w':
#         ep_robot.chassis.move(x=0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
#
#     elif a == 's':
#         ep_robot.chassis.move(x=-0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
#
#     elif a == 'a':
#         ep_robot.chassis.move(x=0, y=-0.5, z=0, xy_speed=0.7).wait_for_completed()
#
#     elif a == 'd':
#         ep_robot.chassis.move(x=0, y=0.5, z=0, xy_speed=0.7).wait_for_completed()
#     else:
#         print("输入有误！！！请重新输入。")
# ###结束机器人程序###


# ep_robot.gimbal.move(pitch=20, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
# ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=3)
# time.sleep(1)
# ep_robot.gimbal.move(pitch=0, yaw=20, pitch_speed=100, yaw_speed=100).wait_for_completed()
# ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
# def shootA():
#     for i in range(4):
#         ep_robot.chassis.move(x=0.5,y=0,z=0,xy_speed=0.7).wait_for_completed()
#         ep_robot.chassis.move(x=0, y=0, z=90, z_speed=30).wait_for_completed()
#         ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE,times=1)
#
# def shootB():
#     ep_robot.chassis.drive_wheels(w1=v[0], w2=v[1], w3=v[1], w4=v[0])
#     ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=3)
#
# def qiqi():
#     ep_robot.chassis.move(x=-0.5,y=0,z=0,xy_speed=0.7)
#
#
# while True:
#     a = input("请控制函数（a/b/c):")
#     if a == 'a':
#         shootA()
#
#     elif a == 'b':
#        shootB()
#
#     elif a=='c':
#         qiqi()
#
#     else:
#         print("输入有误！！！请重新输入。")


def on_detect_marker(marker_info):
    global markers, count
    if marker_info:
        markers = marker_info
        count = 0
    else:
        count += 1
        if count >= 10:
            count = 0
            markers.clear()

markers = []  # 存储识别到的视觉标签数据
count = 0  # 识别次数统计
"""你要写的程序"""

ep_robot.camera.start_video_stream(display=False)  # 打开视频流, 不显示画面
ep_robot.vision.sub_detect_info(name="marker", callback=on_detect_marker)  # 启动摄像头智能识别

while True:
    img = ep_robot.camera.read_cv2_image(strategy="newest")  # 获取最新的一帧视频流
    cv2.imshow("Robot", img)  # 显示图像窗口

    print(markers)  # 打印识别到的标签信息
    if len(markers)!=0:
        if markers[0][4]=='2':
            # ep_robot.chassis.move(x=1,xy_speed=1)
            ep_robot.led.set_led(comp='all',r=111)
        if markers[0][4]=='1':
            # ep_robot.chassis.move(x=-1, xy_speed=1)
            ep_robot.led.set_led(comp='all',g=130)
        if markers[0][4]=='3':
            # ep_robot.chassis.move(x=1,xy_speed=1)
            ep_robot.led.set_led(comp='top_all',r=111,b=90,effect=led.EFFECT_BREATH)
        if markers[0][4]=='4':
            # ep_robot.chassis.move(x=-1, xy_speed=1)
            ep_robot.led.set_led(comp='bottom_all',r=70,g=130,b=90)

    key = cv2.waitKey(40)  # 延时一段时间，并等待按键按下
    if key == 27:  # 按ESC键退出，ESC键的ASCII码是27
        break


ep_robot.camera.stop_video_stream()  # 关闭视频流
cv2.destroyAllWindows()  # 关闭opencv视频窗口

#
# markers = []  # 存储识别到的视觉标签数据
# count = 0  #
#
#
# def on_detect_marker(marker_info):
#     global markers, count
#     if marker_info:
#         markers = marker_info
#         count = 0
#     else:
#         count += 1
#         if count >= 10:
#             count = 0
#             markers.clear()
#
#
# """你要写的程序"""
# ep_robot.camera.start_video_stream(display=False)  # 打开视频流, 不显示画面
# ep_robot.vision.sub_detect_info(name="marker", callback=on_detect_marker)  # 启动摄像头智能识别
# font = cv2.FONT_HERSHEY_SIMPLEX  # 定义一种字体
# yellow = (0, 255, 255)
#
# time1 = time.time()
# while True:
#     img = ep_robot.camera.read_cv2_image(strategy="newest")  # 获取最新的一帧视频流
#     print(markers)
#     if markers:
#         marker = markers[0]
#         # 计算中心点坐标和宽高的像素值
#         x, y, w, h = marker[0] * 1280, marker[1] * 720, marker[2] * 1280, marker[3] * 720
#
#         x1 = int((x - w / 2))  # 求矩形对角点坐标，结果取整
#         y1 = int((y - h / 2))
#         x2 = int((x + w / 2))
#         y2 = int((y + h / 2))
#
#         cv2.rectangle(img, (x1, y1), (x2, y2), yellow, 3)
#         cv2.putText(img, f"x={int(x)}", (x1 + 10, y1 + 30), font, 0.8, yellow, 2)
#         cv2.putText(img, f"y={int(y)}", (x1 + 10, y1 + 60), font, 0.8, yellow, 2)
#
#         if x < 620:
#             yaw_speed = -20
#         elif x > 660:
#             yaw_speed = 20
#         else:
#             yaw_speed = 0
#         if y < 340:
#             pitch_speed = 20
#         elif y > 380:
#             pitch_speed = -20
#         else:
#             pitch_speed = 0
#         # print(yaw_speed,pitch_speed)
#         ep_robot.gimbal.drive_speed(pitch_speed=pitch_speed, yaw_speed=yaw_speed)  # 移动云台到中心点
#
#         if 620 <= x <= 660 and 340 <= y <= 380:
#             time2 = time.time()
#             if time2 - time1 > 3:  # 最小间隔2秒发射一次
#                 # ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE)  # 发射激光
#                 ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE,times=2)  # 发射水晶弹
#                 time1 = time2
#     else:
#         ep_robot.gimbal.drive_speed(pitch_speed=0, yaw_speed=0)
#
#     cv2.imshow("Robot", img)  # 显示图像窗口
#
#     key = cv2.waitKey(40)
#     if key == 27:  # 按ESC键退出
#         break
#
# ep_robot.camera.stop_video_stream()  # 关闭视频流
# cv2.destroyAllWindows()  # 关闭opencv视频窗口
ep_robot.close()
