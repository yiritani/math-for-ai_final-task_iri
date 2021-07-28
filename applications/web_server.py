import base64
import os

import numpy as np
from PIL import Image
from io import BytesIO
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
    return render_template("mainpage.html")


@app.route('/scraping', methods=["GET", "POST"])
def scrape():
    target_url = request.form.get('target_url')

    csv_backup.backup_csv_file()
    scrape_main.scrape_main_func(target_url)

    return render_template("mainpage.html", end_info='Scrape done!')


@app.route('/learning', methods=["GET", "POST"])
def learning():
    controller.main()

    return render_template("mainpage.html", end_info='Learning done!')


@app.route('/show_plot', methods=["GET", "POST"])
def show_plot():
    print('dirname', os.path.dirname(__file__))
    fp = open(str(os.path.dirname(__file__)) + "/machine_learning/output/ScatterRegression.png", "rb")
    sp = base64.b64encode(fp.read()).decode()

    return render_template("mainpage.html", sp=sp, show_flg=True)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
