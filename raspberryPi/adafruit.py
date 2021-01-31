from Adafruit_IO import *
from sound import sound
numb1=0
numb2=0
numb3=0
numb4=0
location="none"
destination ="none"
playing=0
aio = Client('userId','key')
def adafruit():
    location="none"
    destination ="none"
    #location = input("where are you:")
    #destination = input("where you want to go:")    
    #while location!="503":
    while True:
        print("adafruit start")
        if location == "503":
            break
        inputd = input("press 1 to activate:")
        if inputd == "1":
            #file = '/home/pi/sound/arrive.mp3'
            #sound(file,playing)
            numbe = aio.receive("elevator")
            destinationvalue = numbe.value
            print("destinationvalue=%s" %(destinationvalue))
            if destinationvalue == "87":
                 destination = "elevator"
            print("destination=%s" %(destination))
            
            #file = '/home/pi/sound/arrive.mp3'
            #sound(file,playing)
            numbe1 = aio.receive("event1")
            destinationvalue = numbe1.value
            print("destinationvalue=%s" %(destinationvalue))
            if destinationvalue == "87":
                 destination = "event1"
            print("destination=%s" %(destination))
            
            #file = '/home/pi/sound/arrive.mp3'
            #sound(file,playing)
            numbe2 = aio.receive("event2")
            destinationvalue = numbe2.value
            print("destinationvalue=%s" %(destinationvalue))
            if destinationvalue == "87":
                 destination = "event2"
            print("destination=%s" %(destination))
                
            #file = '/home/pi/sound/503.mp3'
            #sound(file,playing)
            numb503 = aio.receive("503")
            locationvalue = numb503.value
            print("locationvalue=%s" %(locationvalue))
            if locationvalue == "87":
                location = "503"
            print("location=%s" %(location))
            print("while end")
            
            
    return location,destination
def adareset():
    print("adareset start")
    reset1 = aio.feeds("503")
    aio.send_data(reset1.key,0)
    
    reset2 = aio.feeds("elevator")
    aio.send_data(reset2.key,0)
    
    reset3 = aio.feeds("event1")
    aio.send_data(reset3.key,0)
    
    reset4 = aio.feeds("event2")
    aio.send_data(reset4.key,0)
    
    reset6 = aio.feeds("linealert")
    aio.send_data(reset6.key,0)
    
#def adastart():
#    print("send line message for departure")
#    a = aio.feeds("linealert")
#    aio.send_data(a.key,87)
    
#def adaend():
#    print("send line message for departure")
#    a = aio.feeds("linealert")
#    aio.send_data(a.key,88)