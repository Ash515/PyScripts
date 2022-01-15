while True:
    x = input("Enter value: ")
    stop_light = int(x)
    if stop_light == 30:
        break
    elif stop_light >= 1 and stop_light < 10:
        print('Green light')
        stop_light += 1
    elif stop_light < 20:
        print('Yellow light')
        stop_light += 1
    elif stop_light < 30:
        print("Red light")
        stop_light += 1
    else:
        stop_light = 0
