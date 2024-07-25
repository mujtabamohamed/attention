import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import db

from dotenv import load_dotenv

load_dotenv('.env')

def add_data_to_database():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('DATABASE_URL'),
    })

    ref = db.reference('Students')

    data = {

        "13579":
            {
                "name": "Elon Musk",
                "department": "IT",
                "total attendance": "8",
                "starting year": "2021",
                "year": "SY",
                "sem": "3",
                "last_attendance_time": "2023-03-05 00:54:34"
            },
    }

    for key, value in data.items():
        ref.child(key).set(value)
