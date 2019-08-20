
# Firebase config
import pyrebase

config = {
    "apiKey": "AIzaSyDBkcfDX1Iufo8remQZdQ1tZwhFy1sirIo",
    "authDomain": "piltover-library.firebaseapp.com",
    "databaseURL": "https://piltover-library.firebaseio.com",
    "projectId": "piltover-library",
    "storageBucket": "piltover-library.appspot.com",
    "messagingSenderId": "49889908321",
    "appId": "1:49889908321:web:561a30a4e89b2909",
    #"serviceAccount": "firebaseconfig/piltover-library-firebase-adminsdk-ieyld-b089b92408.json",
}

__app = pyrebase.initialize_app(config)

auth = __app.auth()
db = __app.database()

# Firebase admin
import firebase_admin
from firebase_admin import credentials, auth as __admin_auth

__cred = credentials.Certificate("firebaseconfig/piltover-library-firebase-adminsdk-ieyld-b089b92408.json")
firebase_admin.initialize_app(__cred)
admin_auth = __admin_auth