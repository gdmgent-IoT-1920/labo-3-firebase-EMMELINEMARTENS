import sense_hat from SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

# constants
COLLECTION = 'raspcollection'
DOCUMENT = 'EmmelineMpi_doc'

# firebase
cred = credentials.Certificate("./config/iotlabo-85706-firebase-adminsdk-wd3oa-d11daf23ba.json")
firebase_admin.initialize_app(cred)

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def update_sensehat(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        if doc_readable.get('matrix').get('isOn'):
                hexdecColor = doc_readable.get('matrix').get('color').get('value')
                print(doc_readable)
                O = list(tuple(int(hexdecColor[i:i+2]),16) for i in ((0,2,4)))
                matrix = [
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O,
                        O,O,O,O,O,O,O,O
                        ]

                sense.set_pixels(matrix)
        else:
                sense.clear()
# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

# app
while True:
    pass
