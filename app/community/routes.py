#Instantiate Blueprint
from flask import Blueprint,render_template


community = Blueprint('community', __name__, template_folder='community_templates')

@community.route('/community')
def ourcommunity():
    return render_template('community.html')