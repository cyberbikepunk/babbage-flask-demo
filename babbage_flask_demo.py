from flask import Flask
from os.path import join, dirname
from sqlalchemy import create_engine
from babbage.manager import JSONCubeManager
from babbage.api import configure_api
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('demo')
engine = create_engine('sqlite:///' + dirname(__file__) + '/cubes.sqlite', echo=True)

app.debug = True
app.config['SECRET_KEY'] = '<replace with a secret key>'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

models_directory = join(dirname(__file__), 'models')
manager = JSONCubeManager(engine, models_directory)
blueprint = configure_api(app, manager)
app.register_blueprint(blueprint, url_prefix='/api/babbage')
toolbar = DebugToolbarExtension(app)




if __name__ == '__main__':
    app.run()
