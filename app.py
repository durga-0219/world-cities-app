from flask import Flask, render_template, request, redirect, url_for
from models import db, Country, City
from utils import load_data
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def setup():
    db.create_all()
    load_data()

@app.route('/')
def index():
    countries = Country.query.order_by(Country.name).all()
    return render_template('index.html', countries=countries)

@app.route('/country')
def redirect_to_country():
    country_id = request.args.get('country_id')
    return redirect(url_for('show_country', country_id=country_id))

@app.route('/country/<int:country_id>')
def show_country(country_id):
    country = Country.query.get_or_404(country_id)
    return render_template('country.html', country=country)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
