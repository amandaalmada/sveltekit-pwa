import pyrebase
from flask import Flask, jsonify, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, Schema
import firebase_admin.auth as auth

firebaseConfig={
  "apiKey": "AIzaSyAxtx_E08rgGWigQs4BrP1us_2Kijl89jw",
  "authDomain": "okymapp-e42bb.firebaseapp.com",
  "projectId": "okymapp-e42bb",
  "storageBucket": "okymapp-e42bb.appspot.com",
  "messagingSenderId": "147080091155",
  "appId": "1:147080091155:web:bad9f99878aea5cc1811e6",
  "measurementId": "G-NQY4L06HWM",
  "databaseURL": "https://okymapp-e42bb-default-rtdb.firebaseio.com/"} 

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = auth.sign_in_anonymous()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SECRET_KEY'] = 'mysupersecretultrasecretkey1234'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
  id = db.Column(db.Integer ,primary_key=True)
  lat_long = db.Column(db.String(200))
  token_id = db.Column(db.String(200))

  def __str__(self):
    return f"id ({self.id}, lat_long{self.lat_long}, token_id{self.token_id})" 
      
class RiskZone(db.Model):
  rz_id = db.Column(db.Integer,primary_key=True)
  rz_lat_long = db.Column(db.String(200))





#guardar_rz = RiskZone(rz_lat_long =rz_uno)
#db.session.add(guardar_rz)
#db.session.commit()
# anonimoo = User(token_id=token_usuario)
# db.session.add(anonimoo)
# db.session.commit()




class SafeZone(db.Model):
  sz_id = db.Column(db.Integer,primary_key=True)
  sz_lat_long = db.Column(db.String(200)) 


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "token_id", "lat_long")


user_schema = UserSchema()
user_schemas = UserSchema(many=True)


class SafeZoneSchema(ma.Schema):
    class Meta:
        fields = ("sz_id", "sz_lat_long")


safe_zone_schema = SafeZoneSchema()
safe_zone_schemas = SafeZoneSchema(many=True)


class RiskZoneSchema(ma.Schema):
    class Meta:
        fields = ("rz_id", "rz_lat_long")


risk_zone_schema = RiskZoneSchema()
risk_zone_schemas = RiskZoneSchema(many=True)


@app.route("/risk-zones")
def risk_zone():
  risk_zones = RiskZone.query.all()
  zonas_de_riesgo = risk_zone_schemas.dump(risk_zones)
  zonas_riesgosas = []
  for risk_zone in zonas_de_riesgo:
    list_zonas_de_riesgo =(risk_zone["rz_lat_long"])
    jzonas_de_riesgo = list_zonas_de_riesgo.split(';') 
    

    for risk_points in jzonas_de_riesgo:
      zonas_riesgosas.append(risk_points.split(', '))
      
  return jsonify(zonas_riesgosas)

@app.route("/safe-zones")
def safe_zone():
    zonas_seguras = [] 
    safe_zones = SafeZone.query.all()
    result_sz= safe_zone_schemas.dump(safe_zones)
    for safe_points in result_sz:
      zonas_seguras_lat = safe_points['sz_lat_long']
      lista_segura = [zonas_seguras_lat] 
      zonas_seguras.append(lista_segura)
    return jsonify(zonas_seguras)


token_usuario = user["idToken"]

@app.route("/sign_in_as_guest")
def guest_user():
  anonimoo = User(token_id=token_usuario)
  db.session.add(anonimoo)
  db.session.commit()
  return (render_template ("home.html")) 

if __name__ == "__main__":
  app.run()


"""@app.route("/")
@app.route("/index", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_pwd']
        try:
            auth.sign_in_with_email_and_password(email,password)
            user_info = auth.sign_in_with_email_and_password(email,password)
            account_info = auth.get_account_info(user_info['idToken'])
            if account_info['user'][o]['emailVerified'] == False:
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
  return render_template ("reset_password.html")"""


# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)