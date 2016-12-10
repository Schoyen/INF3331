from io import BytesIO
from base64 import b64encode
from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_CO2, plot_temperature, plot_CO2_emissions_per_country
from matplotlib.pylab import clf
web_app = Flask(__name__)

@web_app.route("/")
@web_app.route("/index")
def front_page():
    """
    Render front page.

    Returns:
        page:               The rendered front page from templates/index.html.
    """
    return render_template("index.html")

@web_app.route("/co2_data/")
def visualize__initial_co2_data():
    """
    Render site with plots showing the global CO2 emissions per year.

    Returns:
        page:               The initial rendered page with a plot of the emissions.
    """
    clf()
    kwargs = {'show_image': False}
    image = plot_image(plot_CO2, kwargs)
    
    return render_template("co2_data.html", image=image.decode('utf-8'),
            tmin=1751, tmax=2012, ymin=0, ymax=10000)

@web_app.route("/co2_data/handle_input", methods=["POST"])
def visualize_co2_data():
    """
    Render site with plots showing the global CO2 emissions per year.

    This function uses POST-methods.

    Returns:
        page:               The updated page with a plot of the emissions.
    """
    assert request.method == "POST" # Test
    clf() # Clear figure to avoid plotting on top of old image
    image = None
    error_message = []
    error = False

    tmin = int(request.form["tmin"])
    tmax = int(request.form["tmax"])
    ymin = int(request.form["ymin"])
    ymax = int(request.form["ymax"])

    # error handling if min values are greater than max values
    if ymax <= ymin:
        error_message.append("The maximum carbon ({0}) emission must be greater than the minimum ({1}).".format(ymax, ymin))
        error = True

    if tmax <= tmin:
        error_message.append("The final year ({0}) must be greater than the initial year ({1}).".format(tmax, tmin))
        error = True

    # plots image if no errors
    if not error:
        kwargs = {'tmin': tmin, 'tmax': tmax, 'ymin': ymin, 'ymax': ymax, 'show_image': False}
        image = plot_image(plot_CO2, kwargs)

    return render_template("co2_data.html", image=image.decode('utf-8'),
            error=error, error_message=error_message,
            tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax)

@web_app.route("/temperature/")
def visualize_initial_temperature_data():
    """
    Render site with plots showing the average global temperatures per year for a given month.

    Returns:
        page:               The initial page with a plot of the temperatures.
    """
    clf()
    kwargs = {'show_image': False}
    image = plot_image(plot_temperature, kwargs)
    
    return render_template("temperature.html", image=image.decode('utf-8'),
            tmin=1816, tmax=2012, ymin=-6, ymax=1, month="January")

@web_app.route("/temperature/handle_input", methods=["POST"])
def visualize_temperature_data():
    """
    Render site with plots showing the average global temperatures per year for a given month.

    This function uses POST-methods.

    Returns:
        page:               The updated page with a plot of the temperatures.
    """
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

    return render_template("temperature.html", image=image.decode('utf-8'),
            error=error, error_message=error_message,
            tmin=tmin, tmax=tmax, ymin=ymin, ymax=ymax, month=month)

@web_app.route("/co2_by_country/")
def visualize_initial_country_co2():
    """
    Render site with plots showing the CO2 emissions per country for a given year.

    Returns:
        page:               The initial page with a plot of the emissions.
    """
    clf()
    lower_threshold = 8
    upper_threshold = 16
    year=2013
    kwargs = {'lower_threshold': lower_threshold, 'upper_threshold': upper_threshold, 'year': 2013, 'show_image': False}
    image = plot_image(plot_CO2_emissions_per_country, kwargs)
    
    return render_template("co2_by_country.html", image=image.decode('utf-8'),
            year=year, lower_threshold=lower_threshold, upper_threshold=upper_threshold)

@web_app.route("/co2_by_country/handle_input", methods=["POST"])
def visualize_country_co2():
    """
    Render site with plots showing the CO2 emissions per country for a given year.

    This function uses POST-methods.

    Returns:
        page:               The updated page with a plot of the emissions.
    """
    assert request.method == "POST" # Test that we are in POST-mode
    clf() # Clear current figure
    image = None
    error_message = []
    error = False

    year = int(request.form["year"])
    lower_threshold = float(request.form["lower_threshold"])
    upper_threshold = float(request.form["upper_threshold"])

    # error handling if lower threshold is greater or equal to upper threshold
    if upper_threshold <= lower_threshold:
        error_message.append("The upper threshold for carbon emission ({0}) must be greater than the lower threshold ({1}).".format(upper_threshold, lower_threshold))
        error = True

    if not error:
        kwargs = {'lower_threshold': lower_threshold, 'upper_threshold': upper_threshold, 'year': year, 'show_image': False}
        image = plot_image(plot_CO2_emissions_per_country, kwargs)
        
    return render_template("co2_by_country.html", image=image.decode('utf-8'),
            error=error, error_message=error_message,
            year=year, lower_threshold=lower_threshold, upper_threshold=upper_threshold)


def plot_image(plot_func, kwargs):
    """
    Save the plot in a byte buffer and return the image.

    Returns:
        image:              The plot as a byte-buffer.
    """
    
    image_file = BytesIO()
    kwargs['SAVEFIG'] = image_file
    plot_func(**kwargs)
    image_file.seek(0)
    image = b64encode(image_file.getvalue())
    
    return image

if __name__ == '__main__':
    web_app.run(debug=True)
