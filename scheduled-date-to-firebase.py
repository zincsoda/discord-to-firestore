import config
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


# initializations 
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
ref = db.collection('Quotes')
docs = ref.stream()
for doc in docs:
    main_doc = doc
    break
doc_ref = db.collection('Quotes').document(main_doc.id)

def write_to_firebase_quotes(message):
    doc_ref.set({ 'quotes':message, })


def get_days_left_to_birthday():
    # target_date_str = input("Enter the target date (yyyy-mm-dd): ")
    target_date_str = "2023-07-07"
    target_date = datetime.datetime.strptime(target_date_str, '%Y-%m-%d')

    # Get today's date
    today = datetime.datetime.today()

    # Calculate the number of seconds between today's date and the target date
    delta = target_date - today
    seconds_left = delta.total_seconds()

    # Convert seconds to days
    days_left = seconds_left / (60 * 60 * 24)

    # Round to the nearest half day
    half_day = 60 * 60 * 12
    rounded_days_left = round(days_left * 2) / 2

    def days_to_words(days):
        if days == 0:
            return "today"
        elif days == 0.5:
            return "tomorrow morning"
        elif days == -0.5:
            return "yesterday morning"
        elif days > 0:
            return f"in {int(days)} and a half days"
        else:
            return f"{int(-days)} and a half days ago"

    # Display the result
    # print(f"Days left until {target_date_str}: {rounded_days_left:.1f}")
    msg = f"Zuleika's birthday is {days_to_words(rounded_days_left)}"
    write_to_firebase_quotes(msg)
    print(f"Zuleika's birthday is {days_to_words(rounded_days_left)}")

if __name__=="__main__":
    # write_to_firebase_quotes('testing')
    get_days_left_to_birthday()
