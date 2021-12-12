# Flask app for Twitter
import os
import json
# import mkclouds as mc
from twitapp.mkclouds import makeCloud
import base64
from io import BytesIO

from flask import Flask, render_template, url_for, request, Response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'twitapp.sqlite'),
    )

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
    class NameForm(FlaskForm):
        name = SelectField('Click to select a search term:', validators=[DataRequired()], choices=['love', 'hate', 'good', 'disgusting', 'awful', 'best', 'awesome', 'dinner', 'lunch', 'late', 'really', 'gordita', 'chalupa', 'drunk', 'pizza'])
        submit = SubmitField('Submit')
        bootstrap.init_app(app)
        

    @app.route('/')
    def dash():
        return render_template("dash.html")

    @app.route('/about')
    def about():
        return render_template("about.html")
    
    @app.route('/cloud', methods=['GET', 'POST'])
    def cloud():
        # drop_list = ['love', 'hate', 'good', 'disgusting', 'awful', 'best', 'awesome', 'dinner', 'lunch', 'late', 'really', 'gordita', 'chalupa', 'drunk', 'pizza']
        # return render_template("cloud.html", dropdown_list=drop_list)
        name = None
        form = NameForm()
        form.choices = name
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
            if request.method == 'POST':
                buf = BytesIO()
                makeCloud(name).savefig(buf, format="png")
                data = base64.b64encode(buf.getbuffer()).decode("ascii")
                return render_template('cloud.html', image=data, form=form, name=name)
            elif request.method == 'GET':
                return render_template('cloud.html', form=form, name=name)
        return render_template('cloud.html', form=form, name=name)
        
    @app.route('/vader')
    def vader():
        with open('vader.json') as json_file:
            graphJSON = json.load(json_file)
        return render_template("vader.html", graphJSON=graphJSON)


    return app
# app = create_app()

# if __name__ == "__main__":
#     create_app().run()
