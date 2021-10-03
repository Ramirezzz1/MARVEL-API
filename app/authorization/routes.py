from flask import Blueprint
from flask.templating import render_template
from werkzeug.utils import redirect

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods=['Get'])
def login():
    return render_template('login.html')