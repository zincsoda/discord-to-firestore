import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# initializations 
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


ref = db.collection('Quotes')
docs = ref.stream()

print("Docs:")
for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))
    main_doc = doc
    break

doc_ref = db.collection('Quotes').document(main_doc.id)
doc_ref.set({

    'quotes':'test',
})
