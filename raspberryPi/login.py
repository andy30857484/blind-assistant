import os
import time

infoFile="/home/pi/firebase/userInfo.txt"

while True:
    print('I am gonna reset all your device info. Are you sure?(y/n)')
    print('or you can press (ctr+c) to exit')
    ans = input()
    if(ans == 'y'):
        print('removing all your device info.....')
        a = open(infoFile,"r+")
        a.truncate(0)
        a.close()
        time.sleep(2)
        staff = input("please type your staff's name:")
        customer = input("please type user's name:")
        fp = open(infoFile,"a")
        fp.write(staff + ' ' + customer)
        fp.close()
        print('your device info has been updated successfully!')
        print()
        print()
    elif(ans == 'n'):
        print('okey bye~~')
    else:
        print('okey bye~~')