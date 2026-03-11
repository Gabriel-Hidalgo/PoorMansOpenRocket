def vertical_position(v_vertical, time):
    message=int(v_vertical * time - 0.5 * 9.8 * (time ** 2))
    return message


