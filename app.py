import os 

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


def get_images():
	images = []

	for i in os.listdir(os.path.split(os.path.realpath(__file__))[0]+'/static/algae_images'):
		if i != '.DS_Store':
			images.append("algae_images/" + i)
	return images

@app.route('/')
@app.route("/index")  
def index():
	return render_template('index.html')

@app.route('/algae')
def algae():
	return render_template('algae.html', images=get_images())

@app.route('/museum')
def museum():
	return render_template('museum.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run()
	