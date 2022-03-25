def closest_mod_5(x):
    y = x
    while True:
        if y % 5 == 0:
            return y
        else:
            y += 1
