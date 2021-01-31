import RPi.GPIO as GPIO
import pygame
import numpy as np
import threading
from bluepy.btle import Scanner,DefaultDelegate
from sound import sound
from subroutine import path,now,check,wrongway,way
from adafruit import adareset,adafruit
from firestore import firestore
from addrConfig import addrAll
#///////////////////////////////////setup///////////////////////////////////
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #beacon1
GPIO.output(26,GPIO.LOW)
GPIO.setup(19,GPIO.OUT) #beacon2
GPIO.output(19,GPIO.LOW)
GPIO.setup(13,GPIO.OUT) #beacon3
GPIO.output(13,GPIO.LOW)
GPIO.setup(6,GPIO.OUT) #beacon4
GPIO.output(6,GPIO.LOW)
GPIO.setup(5,GPIO.OUT) #beacon5
GPIO.output(5,GPIO.LOW)
GPIO.setup(0,GPIO.OUT) #beacon6
GPIO.output(0,GPIO.LOW)
GPIO.setup(11,GPIO.OUT) #beacon7
GPIO.output(11,GPIO.LOW)
GPIO.setup(9,GPIO.OUT) #beacon8
GPIO.output(9,GPIO.LOW)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.LOW)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,GPIO.LOW)

#///////////////////////////////////variables///////////////////////////////////
aa=0 #plaied mp3 
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=0  #found beacon]
B1=B2=B3=B4=B5=B6=B7=B8=B9=B10=B11=B12=0 #beacon1 rssi
All=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
Path=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
B=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
reg=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
soundfile = np.array(['','','','','','','','','','','',''])
creg=0
number=0
count=0
termination=0
playing=0
infoFile="/home/pi/firebase/userInfo.txt"

#///////////////////////////////////subrotine///////////////////////////////////
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        
#/////////////////////////////////main code/////////////////////////////////
if __name__=='__main__':
    result = firestore(infoFile)
    while result != 'fail':
        print("code start")
        if termination == 1:
            #adaend()
            adareset()
        termination=0
        aa,Path,filew,soundfile=path()
        #adastart()
        All=Now=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
        creg=count=0
        if termination == 0 and aa == 0:
            B=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
            while termination<1 :
                GPIO.output(20,GPIO.HIGH)
                devices = Scanner().withDelegate(ScanDelegate()).scan(0.5)
                check(All)        
                a=c=e=g=i=k=m=o=q=s=u=w=playing=0
                setrssi = -65       
                Now=now(B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12)
                creg,count=way(Now,reg,creg,count)
                for dev in devices:
                    #beacon1 503
                    if dev.addr == addrAll[0] :
                        number=0
                        a=1
                        b=0            
                        if a==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B1=dev.rssi
                                if dev.rssi >setrssi and dev.rssi < 0:
                                    print("found1")
                                    GPIO.output(26,GPIO.HIGH)                            
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0: 
                                        file=soundfile[number]
                                        t1=threading.Thread(target = sound, args = (file,playing))                                
                                        t1.start()
                                        playing=1
                                        B[number]=1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:
                                    GPIO.output(26,GPIO.LOW)
                        else:
                            GPIO.output(26,GPIO.LOW)
                            dev.rssi = 0                    
                            B1=dev.rssi
                            a=0
                    #beacon2    
                    if dev.addr == addrAll[1]  :
                        number=1
                        c=1
                        d=0            
                        if c==1:
                            for (adtype, desc, value) in dev.getScanData():                    
                                B2=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found2")
                                    GPIO.output(19,GPIO.HIGH)                                                        
                                    All[number] = 1                           
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                
                                        file=soundfile[number]
                                        #if playing == 1:
                                        #    t1.join()
                                        t2=threading.Thread(target = sound, args = (file,playing))                                
                                        t2.start()
                                        playing=1
                                        B[number]=1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:
                                    GPIO.output(19,GPIO.LOW)
                        else:
                            GPIO.output(19,GPIO.LOW)
                            dev.rssi = 0
                            B2=dev.rssi
                            c=0
                    #beacon3
                    if dev.addr == addrAll[2] :
                        number=2
                        e=1
                        f=0            
                        if e==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B3=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found3")
                                    GPIO.output(13,GPIO.HIGH)                            
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)    
                                    if B[number]==0 and endw==0:                                
                                        file=soundfile[number]
                                        t3=threading.Thread(target = sound, args = (file,playing))                                
                                        t3.start()
                                        B[number]=1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:
                                    GPIO.output(13,GPIO.LOW)
                        else:
                            GPIO.output(13,GPIO.LOW)
                            dev.rssi = 0
                            B3=dev.rssi
                            e=0
                    #beacon4
                    if dev.addr == addrAll[3] :
                        number=3
                        g=1
                        h=0            
                        if g==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B4=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found4")
                                    GPIO.output(6,GPIO.HIGH)                           
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                
                                        file=soundfile[number]    
                                        t4=threading.Thread(target = sound, args = (file,playing))                                
                                        t4.start()
                                        B[number]=1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:
                                    GPIO.output(6,GPIO.LOW)
                        else:
                            GPIO.output(6,GPIO.LOW)
                            dev.rssi = 0
                            B4=dev.rssi
                            g=0
                    #beacon5
                    if dev.addr == addrAll[4] :
                        number=4
                        i=1
                        j=0            
                        if i==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B5=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found5")
                                    GPIO.output(21,GPIO.HIGH)                            
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B) 
                                    if B[number]==0 and endw==0:                                
                                        file=soundfile[number]
                                        t5=threading.Thread(target = sound, args = (file,playing))                                
                                        t5.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:
                    
                                    GPIO.output(21,GPIO.LOW)
                        else:
                            GPIO.output(21,GPIO.LOW)
                            dev.rssi = 0
                            B5=dev.rssi
                            i=0
                    #beacon6
                    if dev.addr == addrAll[5] :
                        number=5
                        k=1
                        l=0            
                        if k==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B6=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found6")
                                    GPIO.output(5,GPIO.HIGH)                           
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                
                                        file=soundfile[number]
                                        t6=threading.Thread(target = sound, args = (file,playing))                                
                                        t6.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                       
                                else:            
                                    GPIO.output(5,GPIO.LOW)
                        else:
                            GPIO.output(5,GPIO.LOW)
                            dev.rssi = 0
                            B6=dev.rssi
                            k=0
                    #beacon7
                    if dev.addr == addrAll[6] :
                        number=6
                        m=1
                        n=0            
                        if m==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B7=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found7")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t7=threading.Thread(target = sound, args = (file,playing))                                
                                        t7.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B7=dev.rssi
                            m=0
                            
                    #beacon8
                    if dev.addr == addrAll[7] :
                        number=7
                        o=1
                        p=0            
                        if o==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B8=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found8")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t8=threading.Thread(target = sound, args = (file,playing))                                
                                        t8.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B8=dev.rssi
                            o=0
                    #beacon9
                    if dev.addr == addrAll[8] :
                        number=8
                        q=1
                        r=0            
                        if q==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B9=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found9")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t9=threading.Thread(target = sound, args = (file,playing))                                
                                        t9.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B9=dev.rssi
                            q=0
                    #beacon10
                    if dev.addr == addrAll[9] :
                        number=9
                        s=1
                        t=0            
                        if s==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B10=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found10")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t10=threading.Thread(target = sound, args = (file,playing))                                
                                        t10.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B10=dev.rssi
                            s=0
                    #beacon11
                    if dev.addr == addrAll[10] :
                        number=10
                        u=1
                        v=0            
                        if u==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B11=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found11")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t11=threading.Thread(target = sound, args = (file,playing))                                
                                        t11.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B11=dev.rssi
                            u=0
                    #beacon12
                    if dev.addr == addrAll[11] :
                        number=11
                        w=1
                        x=0            
                        if w==1:
                            for (adtype, desc, value) in dev.getScanData():
                                B12=dev.rssi
                                if dev.rssi > setrssi and dev.rssi < 0:
                                    print("found12")
                                    GPIO.output(0,GPIO.HIGH)
                                    All[number] = 1
                                    B[number],endw = wrongway(All,Path,number,B)
                                    if B[number]==0 and endw==0:                                    
                                        file=soundfile[number]
                                        t12=threading.Thread(target = sound, args = (file,playing))                                
                                        t12.start()
                                        B[number] = 1
                                    if soundfile[number] == "/home/pi/sound/arrive.mp3":
                                        dev.rssi=0
                                        B[number]=endw=0
                                        termination=1
                                else:           
                                    GPIO.output(0,GPIO.LOW)
                        else:
                            GPIO.output(0,GPIO.LOW)
                            dev.rssi = 0
                            B12=dev.rssi
                            w=0
                #led show beacon1 found or not(6 sec)
                if a==0:
                    b=b+1
                    if b>4:
                        GPIO.output(26,GPIO.LOW)
                        B1=0
                else:
                    b=0   
                #led show beacon2 found or not(6 sec)
                if c==0:
                    d=d+1
                    if d>4:
                        GPIO.output(19,GPIO.LOW)
                        B2=0
                else:
                    d=0        
                #led show beacon3 found or not(6 sec)
                if e==0:
                    f=f+1
                    if f>4:
                       GPIO.output(13,GPIO.LOW)
                       B3=0
                else:            
                    f=0        
                #led show beacon4 found or not(6 sec)    
                if g==0:
                    h=h+1
                    if h>4:
                       GPIO.output(6,GPIO.LOW)
                       B4=0
                else:
                    h=0        
                #led show beacon5 found or not(6 sec)    
                if i==0:
                    j=j+1
                    if j>4:
                       GPIO.output(21,GPIO.LOW)
                       B5=0
                else:
                    j=0       
                #led show beacon6 found or not(6 sec)    
                if k==0:
                    l=l+1
                    if l>4:
                       GPIO.output(5,GPIO.LOW)
                       B6=0
                else:
                    l=0       
                #led show beacon7 found or not(6 sec)
                if m==0:
                    n=n+1
                    if n>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    n=0
                #led show beacon8 found or not(6 sec)
                if o==0:
                    p=p+1
                    if p>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    p=0
                #led show beacon9 found or not(6 sec)
                if q==0:
                    r=r+1
                    if r>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    r=0
                #led show beacon10 found or not(6 sec)
                if s==0:
                    t=t+1
                    if t>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    t=0
                #led show beacon11 found or not(6 sec)
                if u==0:
                    v=v+1
                    if v>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    v=0
                #led show beacon12 found or not(6 sec)
                if w==0:
                    x=x+1
                    if x>4:
                       GPIO.output(0,GPIO.LOW)
                       B7=0
                else:
                    x=0
                #show beacon1&2 rssi
                print("B1=%s" %(B1))
                print("B2=%s" %(B2))
                print("B3=%s" %(B3))
                print("B4=%s" %(B4))
                print("B5=%s" %(B5))
                print("B6=%s" %(B6))
                print("B7=%s" %(B7))
                print("B8=%s" %(B8))
                print("B9=%s" %(B9))
                print("B10=%s" %(B10))
                print("B11=%s" %(B11))
                print("B12=%s" %(B12)) 
                print()
                
        
        


