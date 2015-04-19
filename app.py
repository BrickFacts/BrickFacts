from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)
app.debug = True

views = 0

@app.route("/")
def index():
  global views
  views += 1
  facts = open('facts.txt').read().splitlines()
  fact =random.choice(facts)

  return render_template('index.html', fact=fact, views=views)

@app.route("/api")
def api():
  print('hi')
  facts = open('facts.txt').read().splitlines()
  fact =random.choice(facts)
  return jsonify({ 'fact' : fact })

@app.route("/apiman")
def apiman():
  return render_template('api.html')

if __name__ == "__main__":
  app.run()

