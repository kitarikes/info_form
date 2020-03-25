from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_sample.database import init_db
from flask_sample.models import Info

def create_app():
  app = Flask(__name__)

  app.config.from_object('flask_sample.config.Config')
  init_db(app)

  return app

app = create_app()
app.secret_key = "aaa"
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
  if request.method == 'GET':
    return render_template('info.html')
  else:
    results = request.form
    db.session.add(Info(name=results['name'], subject=results['subject'], affiliation=results['affiliation'], email=results['email'], contents=results['contents']))
    db.session.commit()
    return render_template('finished.html')

@app.route('/confirm', methods=['POST'])
def confirm():
  results = request.form
  return render_template('confirm.html', name=results['name'], subject=results['subject'], affiliation=results['affiliation'], email=results['email'], contents=results['contents'])

@app.route('/admin', methods=['GET'])
def admin():
  infos = db.session.query(Info).all()
  dict_ = [info.get_detail() for info in infos]

  return render_template('db_table.html', data=dict_)