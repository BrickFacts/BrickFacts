from flask import Flask, render_template, jsonify, flash, request
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Length, Email
import random, twilio.twiml

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'G00DB33F'
app.config['DEBUG'] = True

views = 0

@app.route("/")
def index():
  global views
  views += 1
  fact = rand_fact()

  return render_template('index.html', fact=fact, views=views)

@app.route("/api")
def api():
  return jsonify({ 'fact' : rand_fact() })

@app.route("/apiman")
def apiman():
  return render_template('api.html')

@app.route("/incoming", methods=['GET', 'POST'])
def respond():
  """ Responds with a fact """
  from_number = request.values.get('From', None)
  message = 'Brick Fact: '
  message += rand_fact()

  resp = twilio.twiml.Response()
  resp.message(message)
  return str(resp)

@app.route("/joke", methods=['GET', 'POST'])
def joke():
  jokes = open('jokes.txt').read().splitlines()
  joke = random.choice(jokes)
  return jsonify({ 'joke' : joke })


def rand_fact():
  """ The crown jewels!!!! """
  facts = open('facts.txt').read().splitlines()
  fact = random.choice(facts)
  return fact


###### FORMS #####

class PhoneForm(Form):
  phone_num = IntegerField('Phone Number', validators = [Required(), Length(9,10)])
  submit = SubmitField('Submit')



if __name__ == "__main__":
  app.run()
