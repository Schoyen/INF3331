from io import BytesIO
from base64 import b64encode
from flask import Flask, render_template
from temperature_CO2_plotter import plot_CO2
web_app = Flask(__name__)

@web_app.route("/")
def front_page():
    return render_template("index.html")

@web_app.route("/co2/")
def visualize_co2_data():
    image_file = BytesIO()
    plot_CO2(show_image=False, SAVEFIG=image_file)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    return render_template("co2_data.html", image=image)

if __name__ == '__main__':
    web_app.run(debug=True)
