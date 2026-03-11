# Rocket Launch Calculator
import sys
from trajectory_EBERT import trajectory
import pandas as pd
print("------Rocket Launch Calculator------")

# Input Evaluation
dry_weight = float(input("Enter the dry weight of the rocket in kilograms: "))
if dry_weight <= 0:
    print("Error, invalid weight entered.")
    sys.exit()
    
rocket_length = float(input("Enter the length of the rocket in meters: "))
if rocket_length <= 0:
    print("Error, invalid length entered.")
    sys.exit()
    
rocket_diameter = float(input("Enter the outer diameter of the rocket in meters: "))
if rocket_diameter <= 0:
    print("Error, invalid diameter entered.")
    sys.exit()
    
fuel_weight = float(input("Enter the weight of the fuel in kilograms: "))
if fuel_weight <= 0:
    print("Error, insufficient or invalid fuel quantity entered.")
    sys.exit()

drag_coefficient = float(input("Enter the drag coefficient: "))
if drag_coefficient < 0:
    print("Error, invalid drag coefficient entered.")
    sys.exit()
 
launch_angle = float(input("Enter the launch angle from the horizontal in degrees (between 0 and 180 degrees): "))
if not 0 <= launch_angle <= 180:
    print("Abnormal launch angle, adjust in order to get a proper flight.")
    sys.exit()

burn_time = float(input("Enter the burn time in seconds: "))
if burn_time <= 0:
    print("Error, invalid burn time entered.")
    sys.exit()

thrust = float(input("Enter the thrust produced by the rocket in newtons: "))
if thrust <= 0:
    print("Error, insufficient or invalid thrust quantity entered.")

# Calculations
from math import pi, sin, cos, radians, sqrt, atan
rocket_radius = rocket_diameter/2
area = (pi * rocket_radius ** 2)

# solving for drag
air_density_sea = 1.225
e = 2.71828
atmo_height = 8500
current_altitude = 0 # needs to be changed

launch_weight = dry_weight + fuel_weight

force_gravity = launch_weight*9.8
#thrust-grav/mass
# x = x0 + v0t + 1/2 at^2

time = 0
# find the x and y direction velocities after burnout
horizontal_position = 0
positions=[0,0]

#These cant work without the other before it
# New Math
g=9.8
mass = dry_weight + fuel_weight
weight_force = mass * g

launch_angle = radians(launch_angle)

radius = rocket_diameter / 2
area = pi * radius**2

net_force = thrust - weight_force
acceleration = net_force / mass

if acceleration <= 0:
    sys.exit("Rocket will not lift off. (thrust too low).")
from aurorahorton import burnout_velocity, range_distance
burnout_V = burnout_velocity(acceleration, burn_time)
v_vertical = burnout_V* sin(launch_angle) # finding points till rocket stops producing more thrust
v_horizontal =  burnout_V * cos(launch_angle)


from GabrielHidalgo import bheight
burnout_height = bheight(acceleration,burn_time)

apogee = burnout_height + (v_vertical**2) / (2 * g)
#test Apogee
from GabrielHidalgo import newApogee

testapogee = newApogee(v_vertical, v_horizontal, burnout_V, burnout_height)
print("TEST APOGEE: ", testapogee)

# TEST time to apogee, time fall, and total flight time
from Flight_Apogee_Time_McKenzie import time_to_apogee, time_fall, total_flight_time

testTOA = time_to_apogee(v_vertical, g)
testTF = time_fall(apogee, g)
testTFT = total_flight_time(burn_time, testTOA, testTF)

print("Test TOA", testTOA)
print("Test TF", testTF)
print("Test TFT", testTFT)

total_flight_time = testTFT
x_range=range_distance(v_horizontal , testTFT)

#time_to_apogee = v_vertical / g

#time_fall = sqrt((2 * apogee) / g)

#total_flight_time = burn_time + time_to_apogee + time_fall
from aurorahorton import range_distance
y_p=[]
x_p=[]
positions = []
horizontal_position = 0
from Vertical_position_Function_Logan import vertical_position
while time < total_flight_time :

    # vertical_position = 0.5 * acceleration * (time ** 2)
    y_position = vertical_position(v_vertical,time)
    horizontal_position = int(v_horizontal * time)
    if y_position < 0:
        break
    y_p.append(y_position)
    x_p.append(horizontal_position)
    positions.append([horizontal_position, y_position])
    time += .5

print(f"Launch weight: {launch_weight:.2f} kg")
print(f"Cross-sectional area: {area:.2f} m^2")
print(f"Launch mass: {mass:.2f} kg")
print(f"Net acceleration during burn: {acceleration:.2f} m/s^2")
print(f"Burnout velocity: {burnout_V:.2f} m/s")
print(f"Burnout height: {burnout_height:.2f} m")
print(f"Estimated apogee: {apogee:.2f} m")
print(f"Total flight time: {testTFT:.2f} s")
print(f"Estimated range: {x_range:.2f} m")
print(f"The trajectory of the rocket fight path follows: {positions}")

trajectory(x_p,y_p)