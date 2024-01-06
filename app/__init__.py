from flask import Flask, render_template
from app.blueprints.dashboard.views import dashboard_blueprint
from app.blueprints.home.views import home_blueprint
from app.dataLoader import get_table_DUMMY_DATA
from app.extensions import db, init_extensions
from .constants import get_formatted_conn
from sqlalchemy.ext.automap import automap_base
import dateutil, datetime
from flask_caching import Cache

def create_app():
    app = Flask(__name__)
    conn = get_formatted_conn() # 'mssql+pyodbc://'+username+':' + pwd + '@'+ server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'
    print(conn)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["CACHE_TYPE"] = "SimpleCache",  # Flask-Caching related configs
    app.config["CACHE_DEFAULT_TIMEOUT"] = 300

    init_extensions(app)
    #cache = Cache(app)
    print(conn)

    with app.app_context():        
        app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
        app.register_blueprint(home_blueprint)
      

    from app.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    from app.filters import strftime
    app.add_template_filter(strftime)
    
    return app


