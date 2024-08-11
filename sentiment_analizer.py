import pickle
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your_user_name",
  password="your_password",
  database="database_name",
)

mycursor = mydb.cursor(buffered=True)

def positive_incriment(message, name):
    query = "Update positive set sentiment = sentiment + 1 where name = \"{}\""
    mycursor.execute(query.format(name))
    mydb.commit()
    if 'camera' in message:
        query = "Update positive set camera = camera + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'battery' in message:
        query = "Update positive set battery = battery + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'storage' or 'space' in message:
        query = "Update positive set storage = storage + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'processor' in message:
        query = "Update positive set processor = processor + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()


def negative_incriment(message, name):
    query = "Update negative set sentiment = sentiment + 1 where name = \"{}\""
    mycursor.execute(query.format(name))
    mydb.commit()
    if 'camera' in message:
        query = "Update negative set camera = camera + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'battery' in message:
        query = "Update negative set battery = battery + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'storage' or 'space' in message:
        query = "Update negative set storage = storage + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()
    if 'processor' in message:
        query = "Update negative set processor = processor + 1 where name = \"{}\""
        mycursor.execute(query.format(name))
        mydb.commit()

def analizer(name, messages):
    model = pickle.load(open('vectorizer.pickle','rb'))
    vector = pickle.load(open('vect.pickle','rb'))
    all_messages = messages.split('.')
    for message in all_messages:
        sentiment = model.predict(vector.transform([message]))
        if sentiment[0]:
            positive_incriment(message, name)
            print("positive")
        else:
            negative_incriment(message, name)
            print("negative")