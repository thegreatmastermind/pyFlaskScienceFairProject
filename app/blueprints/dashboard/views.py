from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify, redirect, g

from app.dataLoader import loadInventoryData
from app.models import tblwidth
import os
from app.extensions import db
from sqlalchemy import text
import pandas as pd
from datetime import datetime

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")


@dashboard_blueprint.route("/")
def home():   
    return render_template('dashboard.html')
