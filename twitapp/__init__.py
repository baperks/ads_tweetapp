# Flask app for Twitter
import os

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'twitapp.sqlite'),
    )

    bootstrap.init_app(app)
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

# bootstrap = Bootstrap(app)

    @app.route('/')
    def dash():
        return render_template("dash.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    return app
# app = create_app()

# if __name__ == "__main__":
#     create_app().run()
