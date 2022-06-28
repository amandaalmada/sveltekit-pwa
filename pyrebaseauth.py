import pyrebase
from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
firebaseConfig={
  "apiKey": "AIzaSyAxtx_E08rgGWigQs4BrP1us_2Kijl89jw",
  "authDomain": "okymapp-e42bb.firebaseapp.com",
  "projectId": "okymapp-e42bb",
  "storageBucket": "okymapp-e42bb.appspot.com",
  "messagingSenderId": "147080091155",
  "appId": "1:147080091155:web:bad9f99878aea5cc1811e6",
  "measurementId": "G-NQY4L06HWM",
  "databaseURL": "https://okymapp-e42bb-default-rtdb.firebaseio.com/"} 
firebase=pyrebase.initialize_app(firebaseConfig)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/okymapp.db'
app.config['SECRET_KEY'] = 'mysupersecretultrasecretkey1234'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lat_long = db.Column(db.String(200))
    google_id = db.Column(db.String(200))
    device_id = db.Column(db.String(200))


class RiskZone(db.Model):
    rz_id = db.Column(db.Integer,primary_key=True)
    rz_lat_long = db.Column(db.String(200))

class SafeZone(db.Model):
    sz_id = db.Column(db.Integer,primary_key=True)
    sz_lat_long = db.Column(db.String(200)) 







































@app.route("/")
@app.route("/index",methods=["GET","POST"])
def index():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_pwd']
        try:
            auth.sign_in_with_email_and_password(email,password)
            user_info = auth.sign_in_with_email_and_password(email,password)
            account_info = auth.get_account_info(user_info['idToken'])
            if account_info['user'][0]['emailVerified'] == False:
                verify_message = 'Por favor verifica tu correo'
                return render_template ('index.html', umessage=verify_message)
            return render_template('home.html')
        except:
                unsuccessful = 'Por favor verifica que los datos ingresados son correctos'
                return render_template('index.html', umessage = unsuccessful)
    return render_template("index.html") 
if __name__ == "__main__":
  app.run()

@app.route("/create_account", methods=['GET','POST'])
def create_account():
  if request.method == 'POST':
    pwd0 = request.form['user_pwd0']
    pwd1 = request.form['user_pwd1']
    if pwd0 == pwd1:
      try:
        email = request.form['user_email']
        password = request.form['user_pwd1']
        new_user = auth.create_user_with_email_and_password(email,password)
        auth.send_email_verification(new_user['idToken'])
        return render_template ("verify_email.html")
      except:
        email_existente = 'Este correo ya existe'
        return render_template ("create_account.html", exist_message=email_existente)
  return render_template("create_account.html")

@app.route("/reset_password", methods=['GET','POST'])
def forget_password():
  return render_template ("reset_password.html")