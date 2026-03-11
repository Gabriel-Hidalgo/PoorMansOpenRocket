import numpy as np
from math import sin
def newApogee(vertVelocity, horzVelocity, boVelocity, boHeight):
    g = 9.8
    
    burnout_angle = np.arctan2(vertVelocity,horzVelocity)
     #Finding the angle at burnout with the velocities at burnout
    
    height_after_thrust = ((boVelocity**2)*(sin(burnout_angle))**2)/(2*g) 
    # Finding the height while factoring in burnout angle
    
    apogeeis = boHeight + height_after_thrust 
    #Total height gained, height from thrust added to the height from it being a projectile
    return apogeeis


def bheight(accel, burn_t):
    burnoutHeight = 0.5*accel*(burn_t**2) 
    #Follows the (1/2)at^2 format to find the height of burnout
    return burnoutHeight
