import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, abort, jsonify
from functions_panda import latest_by_country, average_year, per_capi
from functions_panda import country_list, year_list
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s")
handler = RotatingFileHandler('log_api.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
log.addHandler(handler)


@app.route('/')
def home():
    app.logger.debug(f"Acces a la route index /")
    return "Hello"


@app.route('/latest_by_country/<country>')
def by_country(country):
    """
    This function is used when the app.route is released.
    If the selected contry by the user is in the liste, 
    we call  the function latest_by_country.
    If the country isn't in our liste with logger.error
    we will print a message of error saying that the 
    selected country doesn't exist.
    """
    # on veut la valeur la plus récente des emissions
    # totales pour le pays demandé
    app.logger.info("Lancement de la fonction by_country")
    app.logger.warning(f"Acces a la route: latest_by_country/")
    if country in country_list():
        app.logger.debug(f"route demande: latest_by_country/ {country}")
        return jsonify(latest_by_country(country))
        app.logger.debug(f"Operation reussi: {country}")
    elif country.lower() == country:
        app.logger.debug(f"route demande: latest_by_country/ {country}")
        return jsonify(latest_by_country(country.capitalize()))
        app.logger.debug(f"Operation reussi: {country}")
    else:
        app.logger.error(f"la route demande n'existe pas: {country}")
        return abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    """
    This function is used when the app.route is released.
    If the year selected from the user is in the year's liste,
    we call the function average_by_year.
    If the year choosen isn't in the liste,
    the function will print an error message saying that
    the selected year from the user ,doesn't existe.
    """
    # on cherche la moyenne des émissions totales au niveau mondial
    # pour une année demandée
    app.logger.warning(f"Acces a la route")
    if year in year_list():
        app.logger.debug(f"route demande :/average_by_year/ {year}")
        return jsonify(average_year(year))
    else:
        app.logger.error(f"la route demande n'existe pas: {year}")   
        return abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    """
    This function is used when app.route is released.
    If the country selected from the user is in the liste 
    of countries , we call the function per_capita.
    If the selected country isn't in our liste ,
    the function will print an error message saying that
    the country selected from the user doesn't existe.
    """
    app.logger.warning(f"Acces a la route")    
    if country in country_list():
        app.logger.debug(f"Route demande: /per_capita{country}")
        return jsonify(per_capi(country))
    elif country.lower() == country:
        app.logger.debug(f"route demande: /per_capita {country}")
        return jsonify(per_capi(country.capitalize()))
    else:
        app.logger.error(f"La route demande n'existe pas: {country}")
        return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
