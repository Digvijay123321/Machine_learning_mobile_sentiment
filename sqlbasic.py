import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your_user_name",
  password="your_password",
  database="database_name",
)

mycursor = mydb.cursor()
def back_cursor():
    mydb = mysql.connector.connect(
      host="localhost",
      user="your_user_name",
      password="your_password",
      database="database_name",
    )
    return mydb