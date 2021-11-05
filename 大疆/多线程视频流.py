import cv2
import robomaster
from robomaster import robot
from robomaster import led
import tkinter
from PIL import Image,ImageTk
import threading #要多线程才能运行展示动态的画面
from robomaster import blaster

ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')

mark_list=[]
def on_detect_marker(marker_info): ##回调函数
    for i in range(len(marker_info)):
        mark_list.append(marker_info[i])


ep_robot.camera.start_video_stream(display=False)#打开摄像头视频流，不显示画面
result=ep_robot.vision.sub_detect_info(name="marker",callback=on_detect_marker)
#创建tkinter主窗口
root=tkinter.Tk()
canvas=tkinter.Canvas(root,width=1280,height=720,bg='white')
def display_video(): ####这个是线程执行的函数，功能是不断得到画面
    while True:
        img = ep_robot.camera.read_cv2_image(strategy='newest', timeout=0.5)  # 获取最新的帧（画面）
        #把照片放在画布里显示，
        #数组要转换成图像，才能在tkinter里显示，所以，还需要转变,颜色会有不正常，还需要改变颜色
        cv2image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        im=Image.fromarray(cv2image)
        imgtk=ImageTk.PhotoImage(image=im)
        #画布里添加图片，静态的
        canvas.create_image((640,360),image=imgtk)
        obr=imgtk #起到一个缓存延时的作用,随便定义一个变量即可
        #识别标签



#创建播放视频的线程
t_display=threading.Thread(target=display_video)
t_display.start()
#键盘处理函数
def callback_key(event):
    print(event.char)
    if event.char=="w":
        ep_robot.chassis.move(x=0.5,y=0,z=0,xy_speed=0.5).wait_for_completed()
    elif event.char=="s":
        ep_robot.chassis.move(x=-0.5,y=0,z=0, xy_speed=0.5).wait_for_completed()
    elif event.char=="a":
        ep_robot.chassis.move(x=0,y=-0.5,z=0, xy_speed=0.5).wait_for_completed()
    elif event.char=="d":
        ep_robot.chassis.move(x=0,y=0.5,z=0, xy_speed=0.5).wait_for_completed()
    elif event.char=="r":
        ep_robot.chassis.move(x=0, y=0, z=50, z_speed=0.5).wait_for_completed()
        ep_robot.gimbal.move(yaw=-50,yaw_speed=50).wait_for_completed()
    elif event.char=="t":
        ep_robot.chassis.move(x=0, y=0, z=-50, z_speed=0.5).wait_for_completed()
        ep_robot.gimbal.move(yaw=50, yaw_speed=50).wait_for_completed()
    else:
        ep_robot.chassis.move(x=0,y=0,z=0, xy_speed=0.5).wait_for_completed()
#绑定键盘事件,用回调函数实现
canvas.bind("<Key>",callback_key)#k要大写

def callback_mouse(event):
    print(event.x,event.y)
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE,times=2)

canvas.bind("<Button-1>",callback_mouse)

#跟踪标签，当标签的x小于0.5时（值的范围是0-1），云台往左侧转


#让画布获取焦点
canvas.focus_set()
canvas.pack()
root.mainloop()
ep_robot.close()
