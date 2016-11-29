from io import BytesIO
from base64 import b64encode
from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_CO2, plot_temperature, plot_CO2_emissions_per_country
from matplotlib.pylab import clf
web_app = Flask(__name__)

@web_app.route("/")
def front_page():
    return render_template("index.html")

@web_app.route("/co2_data/")
def visualize__initial_co2_data():
    image_file = BytesIO()
    plot_CO2(show_image=False, SAVEFIG=image_file)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    return render_template("co2_data.html", image=image,
            tmin=1750, tmax=2050, ymin=0, ymax=10000)

@web_app.route("/co2_data/handle_input_co2_data", methods=["Post"])
def visualize_co2_data():
    assert request.method == "POST" # Test
    clf() # Clear figure to avoid plotting on top of old image
    image = None
    error_message = []
    error = False

    tmin = int(request.form["tmin"])
    tmax = int(request.form["tmax"])
    ymin = int(request.form["ymin"])
    ymax = int(request.form["ymax"])

    if ymax <= ymin:
        error_message.append("The maximum carbon ({0}) emission must be greater than the minimum ({1}).".format(ymax, ymin))
        error = True

    if tmax <= tmin:
        error_message.append("The final year ({0}) must be greater than the initial year ({1}).".format(tmax, tmin))
        error = True

    if not error:
        image_file = BytesIO()
        plot_CO2(tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax, show_image=False, SAVEFIG=image_file)
        image_file.seek(0)
        image = b64encode(image_file.getvalue())

    return render_template("co2_data.html", image=image,
            error=error, error_message=error_message,
            tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax)

@web_app.route("/temperature/")
def visualize_initial_temperature_data():
    image_file = BytesIO()
    plot_temperature(show_image=False, SAVEFIG=image_file)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    return render_template("temperature.html", image=image)

@web_app.route("/co2_by_country/")
def visualize_country_co2():
    image_file = BytesIO()
    plot_CO2_emissions_per_country(show_image=False, SAVEFIG=image_file)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    return render_template("co2_by_country.html", image=image)

if __name__ == '__main__':
    web_app.run(debug=True)
