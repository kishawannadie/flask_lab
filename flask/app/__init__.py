from flask import Flask
from common.IOStrategies import *
from common.StorageStrategies import *
from common.Students import *
from flask import render_template

app = Flask(__name__)

from app.groupPickle import bp as bp1
from app.groupSQLite import bp as bp2
from app.groupPostgres import bp as bp3
from app.groupMongoDB import bp as bp4
from app.groupRabbitMQ import bp as bp5

groups = [
    ["PickleStorage Student Group", bp1, "/groupPickle"],
    ["SQLite Student Group", bp2, "/groupSQLite"],
	["PostgreSQL Student Group", bp3, "/postgreSQL"],
 	["MongoDB Student Group", bp4, "/groupMongoDB"],
 	["RabbitMQ Student Group", bp5, "/RabbitMQ"]
  
]

for title, bp, url in groups:
    app.register_blueprint(bp, url_prefix=url)

@app.route("/")
def index():
	r = ""
	for title, bp, url in groups:
		r += f'<a href="{url}">{title}</a><br>'
	return render_template("index.tpl", groups=r)
