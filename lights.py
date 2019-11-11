from phue import Bridge

def lightsOFF():
    b = Bridge('192.168.1.61')
    lights = b.get_light_objects()
    for l in lights:
        l.on=False
    return "Lights off"

def lightsON():
    b = Bridge('192.168.1.61')
    lights = b.get_light_objects()
    for l in lights:
        l.on=True
        #l.brightness=256
        #l.saturation=254
    return "Lights on"

def lightStatus():
    b = Bridge('192.168.1.61')
    lights = b.get_light_objects()
    dataString=""
    for l in lights:
        dataString=dataString+l.name
        if l.on:
            #print(l.xy)
            dataString=dataString+" {:d}% on.\n".format(int(100*l.brightness/254))
        else:
            dataString=dataString+" off.\n"
    if not len(dataString):
        return "No lights"
    return dataString