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
    kwargs = {'show_image': False}
    image = plot_image(plot_CO2, kwargs)
    return render_template("co2_data.html", image=image,
            tmin=1750, tmax=2050, ymin=0, ymax=10000)

@web_app.route("/co2_data/handle_input", methods=["POST"])
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
        kwargs = {'tmin': tmin, 'tmax': tmax, 'ymin': ymin, 'ymax': ymax, 'show_image': False}
        image = plot_image(plot_CO2, kwargs)

    return render_template("co2_data.html", image=image,
            error=error, error_message=error_message,
            tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax)

@web_app.route("/temperature/")
def visualize_initial_temperature_data(): 
    kwargs = {'show_image': False}
    image = plot_image(plot_temperature, kwargs)
    return render_template("temperature.html", image=image,
            tmin=1800, tmax=2050, ymin=-6, ymax=1, month="January")

@web_app.route("/temperature/handle_input", methods=["POST"])
def visualize_temperature_data(): 
    assert request.method == "POST" # Test that we are in POST-mode
    clf() # Clear current figure
    image = None
    error_message = []
    error = False

    month = request.form["month"]
    tmin = int(request.form["tmin"])
    tmax = int(request.form["tmax"])
    ymin = int(request.form["ymin"])
    ymax = int(request.form["ymax"])

    if ymax <= ymin: 
        error_message.append("The maximum temperature ({0}) must be greater than the minimum ({1}).".format(ymax, ymin))
        error = True

    if tmax <= tmin: 
        error_message.append("The final year ({0}) must be greater than the initial year ({1}).".format(tmax, tmin))
        error = True

    if not error: 
        kwargs = {'tmin': tmin, 'tmax': tmax, 'ymin': ymin, 'ymax': ymax, 'month': month, 'show_image': False}
        image = plot_image(plot_temperature, kwargs)

    return render_template("temperature.html", image=image,
            error=error, error_message=error_message,
            tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax, month=month)

@web_app.route("/co2_by_country/handle_input")
def visualize_initial_country_co2(): 
    kwargs = {'show_image': False}
    image = plot_image(plot_CO2_emissions_per_country, kwargs)
    return render_template("co2_by_country.html", image=image)

#@web_app.route("/co2_by_country/")
#def visualize_initial_country_co2(): 
#    kwargs = {'show_image': False}
#    image = plot_image(plot_CO2_emissions_per_country, kwargs)
#    return render_template("co2_by_country.html", image=image)

def plot_image(plot_func, kwargs): 
    image_file = BytesIO()
    kwargs['SAVEFIG'] = image_file
    plot_func(**kwargs)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    return image

if __name__ == '__main__': 
    web_app.run(debug=True)
