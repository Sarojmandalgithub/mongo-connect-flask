from flask import Flask,request,render_template,redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db

class User(db.Model):
   
   id = db.Column(db.Integer,primary_key=True)
   name = db.Column(db.String(100),nullable=False)
   email =db.Column(db.String(100),unique=True)
   password = db.Column(db.String(100))

def _init__(self,email,password,name):
   self.name= name
   self.email= email
   self.password =bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

   def check_password(self,password):
      return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
   
   with app.app_context():
      db.create_all()
      
  
@app.route('/')
def home():
  return 'Hello from flask'

@app.route('/signup',methods=['GET','POST'])
def signup():
   if request.method=='POST':
      #handle request
      name =request.form['name']
      email =request.form['email']
      password =request.form['password']

      new_user = User(name=name,email=email,password=password)
      db.session.add(new_user)
      db.session.commit()
      return redirect('/login')


   return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method=='POST':
      #handle request
      pass
   return render_template('login.html')
   







if __name__=='_main_':
   app.run (debug=True)