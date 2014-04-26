import os
from flask import Flask
import buildGraph
import json
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def hello():
	print "hello"
	return app.send_static_file('wildcat.html')

@app.route('/searchid/<searchid>')
def show_user_profile(searchid):
	# show the user profile for that user
	term_id = searchid.split("&")[0]
	concept = searchid.split("&")[1]
	graph = buildGraph.getGraph(term_id,concept)
	f = open("./static/maps/asia.json","w")
	f.write(json.dumps(graph))
	f.close()
	return app.send_static_file('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)