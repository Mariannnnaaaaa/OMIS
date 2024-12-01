from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('index.html')

@app.route('/cart')
def cart():
  return render_template('cart.html')

@app.route('/catalog')
def catalog():
  return render_template('catalog.html')

@app.route('/favorites')
def favorites():
  return render_template('favorites.html')

@app.route('/history')
def history():
  return render_template('history.html')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/seller')
def seller():
  return render_template('seller.html')

if __name__ == '__main__':
  app.run(debug=True)