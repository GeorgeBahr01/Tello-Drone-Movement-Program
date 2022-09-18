from djitellopy import Tello
import threading
tello=Tello()
tello.connect()

tello.takeoff()
tello.go_xyz_speed(-100,100,-50,50)
tello.go_xyz_speed(100,-100,50,100)
height=tello.get_height()
print(height)
tello.flip_forward()
tello.flip_back()
height=tello.get_height()
print(height)
tello.land()
battery=tello.get_battery()
print(battery)