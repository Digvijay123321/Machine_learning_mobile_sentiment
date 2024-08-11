from flask import Flask, render_template, request, redirect, url_for, session
from bak_db import rows
import mysql.connector
import mysql.connector
from chart import draw_graph
from sentiment_analizer import analizer
from feat2 import mail


mydb = mysql.connector.connect(
  host="localhost",
  user="your_user_name",
  password="your_user_password",
  database="databse_name",
)

mycursor = mydb.cursor(buffered=True)

app = Flask(__name__)
app.secret_key = 'major_project'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return '<User: {self.username}>'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        u_id = request.form["uid"]
        pass_wd = request.form["passwd"]
        if u_id == "admin" and pass_wd =="gcoea":
            session['loggedin'] = True
            return redirect(url_for("admin_page"))
        try:
            qur = "SELECT * FROM logins"
            mycursor.execute(qur)
            account = mycursor.fetchone()
            while account is not None:
                
                if account[3] == pass_wd and account[2] == u_id:
                    session['loggedin'] = True
                    session['id'] = account[0]
                    session['username'] = account[1]
                    return redirect(url_for('home'))
                account = mycursor.fetchone()
        except:
            print(account[0], pass_wd)
            return 'Wrong id or pass word'
    return render_template("login.html")


@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        sql = "INSERT INTO logins (name, email, password) VALUES (\"{}\", \"{}\", \"{}\")"
        mycursor.execute(sql.format(name, email, password))
        mydb.commit()
        mail(email, name)
        mob_names = [item[0] for item in rows]
        a = [item[1] for item in rows]
        return render_template("tp1.html", data = mob_names, img = a, name = name)
    return render_template("register.html")


@app.route('/home')
def home():
    if 'loggedin' in session:
        mob_names = [item[0] for item in rows]
        a = [item[1] for item in rows]
        return render_template("tp1.html", data = mob_names, img = a, name=session['username'])
    return redirect(url_for('login'))



@app.route('/home/<m_name>', methods=['GET', 'POST'])
def mobileSpecifications(m_name):
    if 'loggedin' in session:
        sql = "SELECT * FROM comments WHERE name = \"{}\""
        mycursor.execute(sql.format(m_name))
        comm = mycursor.fetchall()
        desc=[]
        for item in rows:
            if item[0] == m_name:
                desc = item
        img = desc[1]
        if request.method == 'POST':
            new_comment = request.form["comment"]
            sql = "INSERT INTO comments (name, commant, user_name) VALUES (\"{}\", \"{}\", \"{}\")"
            mycursor.execute(sql.format(m_name, new_comment, session['username']))
            mydb.commit()
            analizer(m_name, new_comment)
            return redirect(request.url)
        return render_template('mob_viewer.html', mob = m_name, img = img, desc = desc, comments = comm[::-1])
    return redirect(url_for('login'))

@app.route('/admin')
def admin_page():
    if 'loggedin' in session:
        fet=["sentiment", "camera", "battery", "storage", "processor"]
        image={"sentiment":"fa fa-bar-chart", "camera":"fa fa-camera-retro", "battery":"fa fa-battery-half",
               "storage":"fa fa-folder-open-o", "processor":"fa fa-microchip"}
        return render_template('xyz.html', fet = fet, image = image)
    return render_template("login.html")

@app.route('/admin/<feature>')
def to_graph(feature):
    draw_graph(feature)
    return redirect(url_for('admin_page'))


if __name__ == '__main__':
   app.run(debug = True)
