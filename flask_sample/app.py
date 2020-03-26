from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask_sample.database import init_db
from flask_sample.models import Info

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


ADMIN = os.environ.get("ADMIN")
PASSWORD = os.environ.get("PASSWORD")

def create_app():
  app = Flask(__name__)

  app.config.from_object('flask_sample.config.Config')
  init_db(app)

  return app

app = create_app()
app.secret_key = "111111"
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html', **session)

# お問い合わせフォーム関連
@app.route('/info', methods=['GET', 'POST'])
def info():
  if request.method == 'GET':
    return render_template('info/info.html', **session)
  else:
    results = request.form
    print(results)
    db.session.add(Info(**results))
    db.session.commit()
    return render_template('info/finished.html', **session)

@app.route('/confirm', methods=['POST'])
def confirm():
  results = request.form
  return render_template('info/confirm.html', **results, **session)


# 認証関連
@app.route('/admin', methods=['GET', 'POST'])
def admin():
  if 'admin' in session:
    if session['admin']:
      infos = db.session.query(Info).all()
      dict_ = [info.get_detail() for info in infos]
      try:
        return render_template('db_table.html', data=dict_, **session)
      except:
        return redirect('/info')
  else:
    return redirect('/sign_in')


@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
  if request.method == 'GET':
    return render_template('login/sign_in.html', **session)
  else:
    results = request.form
    if ADMIN == results['username'] and PASSWORD == results['password']:
      session['admin'] = True
      return redirect('/admin')
    else:
      return redirect('/sign_in')

@app.route('/sign_out')
def logout():
    # remove the username from the session if its there
    session.pop('admin', None)
    return redirect('/sign_in')

# db関連
@app.route('/delete', methods=['POST'])
def delete():
  results = request.form.getlist('id')
  for x in results:
    db.session.query(Info).filter(Info.id == int(x)).delete()
    db.session.commit()
  return redirect('/admin')