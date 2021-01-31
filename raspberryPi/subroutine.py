import numpy as np
from Adafruit_IO import *
from sound import sound
from adafruit import adafruit
aio = Client('andy30857484','2f7dc0bb61344dec89722e399b4155cf')
urat503 = '/home/pi/sound/503.mp3'
turnleft3m = '/home/pi/sound/3m_turn_left.mp3'
gostraight = '/home/pi/sound/go_straight.mp3'
keepright = '/home/pi/sound/keep_right.mp3'
turnleft = '/home/pi/sound/turn_left.mp3'
worngway = '/home/pi/sound/worng_way.mp3'
turnright = '/home/pi/sound/turn_right.mp3'
arrive = '/home/pi/sound/arrive.mp3'
none = '/home/pi/sound/503none.mp3'
Path=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
Now=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
B1=B2=B3=B4=B5=B6=B7=B8=B9=B10=B11=B12=0
aa=1
numb1=0
numb2=0
numb3=0
numb4=0
soundfile = np.array(['','','','','','','','','','','',''])
All=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
Path=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
B=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
way=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
Now=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
reg=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
creg=0
count=0
number=0
playing=0
filew='/home/pi/sound/worng_way.mp3'
#-----------------------------------------------------------------------------------
def wrongway (All,Path,number,B):
    endw=0
    termination=0
    for kkk in range (0,12):
        if All[kkk] == 1:
            if Path[kkk] == 0:
                B[number]=2
                kkk=11
    if B[number]==0:
        B[number]=0
    if B[number]==2:
        print("u r in the worng way")
        file=filew
        end=sound(file,playing)
        if end==0:
            B[number]=0
        endw=1
    return B[number],endw
#-----------------------------------------------------------------------------------
def way(Now,reg,creg,count):
    print("way start!!!")
    for ii in range(0,12):
        if Now[ii]!=0:
            count=ii+1
    if count >= creg:
        print("OK")
        creg=count
    if count < creg:
        print("not OK")
        print("not OK")
        print("not OK")
        print("not OK")
        print("not OK")
        print("not OK")
        print("not OK")
        print("u r in the worng way77")
        file=filew
        end=sound(file,playing)
        creg=count
    return creg,count
#-----------------------------------------------------------------------------------
def path():
        print("path start")
        #location = input("where are you:")
        #destination = input("where you want to go:")
        aa=1
        location,destination=adafruit()
        if location == "503" and destination == "elevator" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = gostraight
            fileb3 = none
            fileb4 = none
            fileb5 = turnleft3m
            fileb6 = turnleft
            fileb7 = arrive
            fileb8 = none
            fileb9 = none
            fileb10= none
            fileb11= none
            fileb12= none
            #plan the path
            aa=0
            Path = np.array([1,1,1,1,1,1,1,0,0,0,0,0])
            print(Path)
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile
            
        if location == "503" and destination == "504" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = arrive
            fileb3 = none
            fileb4 = none
            fileb5 = none
            fileb6 = none
            fileb7 = none
            fileb8 = none
            fileb9 = none
            fileb10= none
            fileb11= none
            fileb12= none
            #plan the path
            aa=0
            Path = np.array([1,1,0,0,0,0,0,0,0,0,0,0])
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile
            
        if location == "503" and destination == "504-1" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = gostraight
            fileb3 = arrive
            fileb4 = none
            fileb5 = none
            fileb6 = none
            fileb7 = none
            fileb8 = none
            fileb9 = none
            fileb10= none
            fileb11= none
            fileb12= none
            #plan the path
            aa=0
            Path = np.array([1,1,1,0,0,0,0,0,0,0,0,0])
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile

        if location == "503" and destination == "505" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = gostraight
            fileb3 = none
            fileb4 = arrive
            fileb5 = none
            fileb6 = none
            fileb7 = none
            fileb8 = none
            fileb9 = none
            fileb10= none
            fileb11= none
            fileb12= none
            #plan the path
            aa=0
            Path = np.array([1,1,1,1,0,0,0,0,0,0,0,0])
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile

        if location == "503" and destination == "event2" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = turnleft
            fileb3 = none
            fileb4 = none
            fileb5 = none
            fileb6 = none
            fileb7 = none
            fileb8 = none
            fileb9 = arrive
            fileb10= none
            fileb11= none
            fileb12= none
            #plan the path
            aa=0
            Path = np.array([1,1,0,0,0,0,0,0,1,0,0,0])
            print(Path)
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile

        if location == "503" and destination == "event1" :
            #setup the mp3 files
            filew  = worngway
            fileb1 = urat503
            fileb2 = turnleft
            fileb3 = none
            fileb4 = none
            fileb5 = none
            fileb6 = none
            fileb7 = none
            fileb8 = none
            fileb9 = turnright
            fileb10= none
            fileb11= gostraight
            fileb12= arrive
            #plan the path
            aa=0
            Path = np.array([1,1,0,0,0,0,0,0,1,0,1,1])
            print(Path)
            soundfile = np.array([fileb1,fileb2,fileb3,fileb4,fileb5,fileb6,fileb7,fileb8,fileb9,fileb10,fileb11,fileb12])
            return aa,Path,filew,soundfile
        else:
            aa=1
            Path = np.array([1,0,0,0,0,0,0,1,0,0,1,1])
            soundfile = np.array(["","","","","","","","","","","",""])
            filew=""
            return aa,Path,filew,soundfile
#-----------------------------------------------------------------------------------    
def now(B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12):
    print("now start")
    if B1 > -68 and B1 < 0:
        Now[0]=1
    else:
        Now[0]=0
    if B2 > -68 and B2 < 0:
        Now[1]=1
    else:
        Now[1]=0
    if B3 > -68 and B3 < 0:
        Now[2]=1
    else:
        Now[2]=0
    if B4 > -68 and B4 < 0:
        Now[3]=1
    else:
        Now[3]=0
    if B5 > -68 and B5 < 0:
        Now[4]=1
    else:
        Now[4]=0
    if B6 > -68 and B6 < 0:
        Now[5]=1
    else:
        Now[5]=0
    if B7 > -68 and B7 < 0:
        Now[6]=1
    else:
        Now[6]=0
    if B8 > -68 and B8 < 0:
        Now[7]=1
    else:
        Now[7]=0
    if B9 > -68 and B9 < 0:
        Now[8]=1
    else:
        Now[8]=0
    if B10 > -68 and B10 < 0:
        Now[9]=1
    else:
        Now[9]=0
    if B11 > -68 and B11 < 0:
        Now[10]=1
    else:
        Now[10]=0
    if B12 > -68 and B12 < 0:
        Now[11]=1
    else:
        Now[11]=0
    print("Now=%s" %(Now))
    return Now
#-----------------------------------------------------------------------------------
def check(All):
    print()
    print("check start")
    for ii in range(0,12):
        if ii == 0:
            if All[ii] == 0:
                print("1 503")
            if All[ii] == 1:
                print("1 503 check!")
        if ii == 1:
            if All[ii] == 0:
                print("2 504")
            if All[ii] == 1:
                print("2 504 check!")
        if ii == 2:
            if All[ii] == 0:
                print("3 504")
            if All[ii] == 1:
                print("3 504-1 check!")
        if ii == 3:
            if All[ii] == 0:
                print("4 505")
            if All[ii] == 1:
                print("4 505 check!")
        if ii == 4:
            if All[ii] == 0:
                print("5 corridor1")
            if All[ii] == 1:
                print("5 corridor1 check!")
        if ii == 5:
            if All[ii] == 0:
                print("6 elevator")
            if All[ii] == 1:
                print("6 elevator check!")
        if ii == 6:
            if All[ii] == 0:
                print("7 corridor2")
            if All[ii] == 1:
                print("7 corridor2 check!")
        if ii == 7:
            if All[ii] == 0:
                print("8 event1")
            if All[ii] == 1:
                print("8 event1 check!")
        if ii == 8:
            if All[ii] == 0:
                print("9 garden1")
            if All[ii] == 1:
                print("9 garden1 check!")
        if ii == 9:
            if All[ii] == 0:
                print("10 garden2")
            if All[ii] == 1:
                print("10 garden2 check!")
        if ii == 10:
            if All[ii] == 0:
                print("11 event2")
            if All[ii] == 1:
                print("11 event2 check!")
        if ii == 11:
            if All[ii] == 0:
                print("12 garden3")
            if All[ii] == 1:
                print("12 garden3 check!")
    print()