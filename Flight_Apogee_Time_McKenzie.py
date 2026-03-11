from math import sqrt
def time_to_apogee(v_vertical, g):
    message = int(v_vertical / g)
    return message

def time_fall(apogee, g):
    message2 = int(sqrt((2 * apogee) / g))
    return message2

def total_flight_time(burn_time, time_to_apogee1, time_fall):
    message3 = int(burn_time) + int(time_to_apogee1) + int(time_fall)
    return message3



#time_to_apogee = v_vertical / g

#time_fall = sqrt((2 * apogee) / g)
#total_flight_time = burn_time + time_to_apogee + time_fall

#range_distance = v_horizontal * total_flight_time