import base64
import os

from flask import *
from scrape import csv_backup
from scrape import scrape_main
from machine_learning import controller

app = Flask(__name__, static_folder='machine_learning/output')


@app.route("/")
def red():
    return redirect('/index')


@app.route("/index", methods=["GET", "POST"])
def main_page():
    fp = open(str(os.path.dirname(__file__)) + "/templates/img/suumo_comment.png", "rb")
    sp = base64.b64encode(fp.read()).decode()

    return render_template("index.html", sp=sp)


@app.route('/scraping', methods=["GET", "POST"])
def scrape():
    target_url = request.form.get('target_url')

    csv_backup.backup_csv_file()
    scrape_main.scrape_main_func(target_url)

    return render_template("learn.html", end_info='Scrape done!')


@app.route('/learning_before', methods=["GET", "POST"])
def learning_before():
    return render_template("learn.html")


@app.route('/learning', methods=["GET", "POST"])
def learning():
    station = request.form.get('far_from_station')
    age = request.form.get('age')
    price = request.form.get('price')

    controller.main(float(station), float(age), float(price))

    print('\033[31m' + 'show_plot START' + '\033[0m')
    fp = open(str(os.path.dirname(__file__)) + "/machine_learning/output/ScatterRegression.png", "rb")
    sp = base64.b64encode(fp.read()).decode()

    return render_template("learned.html", end_info='Learning done!', sp=sp, show_flg=True, station=station, age=age, price=price)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
