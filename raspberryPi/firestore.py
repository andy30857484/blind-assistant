import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate("/home/pi/firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
infoFile="/home/pi/firebase/userInfo.txt"
db=firestore.client()



def firestore(infoFile):
    print('getting your device info.......')
    print()
    info = open(infoFile,"r").read()
    a = info.split()
    Id = a[0]
    user = a[1]
    
    try:
        status_ref=db.collection(u'device').document(Id)
        status=status_ref.get()
        
        customer = format(status.to_dict()[u'customer'])
        device = format(status.to_dict()[u'device'])
        rssi = format(status.to_dict()[u'rssi'])
        staff = format(status.to_dict()[u'staff'])
        
        if(user == customer):
            print("here is your device info:")
            print('{')
            print("customer:%s" %(customer))
            print("device:%s" %(device))
            print("rssi:%s" %(rssi))
            print("staff:%s" %(staff))
            print('}')
            print()
            return 'sucess'
        else:
            print("can not find this customer")
            return 'fail'
            
    except:
        print("can not find this staff")
        return 'fail'
    


