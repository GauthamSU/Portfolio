from flask import Flask, render_template  #, jsonify

webapp = Flask(__name__)


@webapp.route('/')
def hello():
  return render_template('home_page.html')


@webapp.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  webapp.run(host='0.0.0.0', debug=True)
