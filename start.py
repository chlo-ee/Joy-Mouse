#! /usr/bin/env python
import pygame, sys, pymouse, os, time
from Xlib import display

pygame.init()
before=0
joysticks=list()
mouse = pymouse.PyMouse()
def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

for i in xrange(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
   
while True:
    pygame.event.pump()
    print ('Count: %d Axis0: %s Axis1: %s Axis2: %s Axis3: %s Hat: %s'
               % (len(joysticks),
                  joystick.get_axis(0),
                  joystick.get_axis(1),
                  joystick.get_axis(2),
                  joystick.get_axis(3),
                  joystick.get_hat(0)))
    positions=mousepos()
    if joystick.get_button(2)==1:
        if before!=2:
            print "mouse.click("+str(positions[0])+","+str(positions[1])+",1)"
            mouse.click(positions[0],positions[1],2)
            before=2
    elif joystick.get_button(0)==1:
        if before!=1:
            print "mouse.click("+str(positions[0])+","+str(positions[1])+",1)"
            mouse.click(positions[0],positions[1],1)
            before=1
    else:
        before = 0
    
    if joystick.get_hat(0)[0] == -1:
        os.system('xte "key Left"')
    if joystick.get_hat(0)[0] == 1:
        os.system('xte "key Right"')
    if joystick.get_hat(0)[1] == -1:
        os.system('xte "key Down"')
    if joystick.get_hat(0)[1] == 1:
        os.system('xte "key Up"')
    
    mouse.move(positions[0]+joystick.get_axis(0)*10, positions[1]+joystick.get_axis(1)*10)
    time.sleep(0.02)              
    
 

