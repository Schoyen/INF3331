from matplotlib.pylab import plot, show, axis, savefig, xlabel, ylabel, title, bar, xticks, axhline, legend, figure, tight_layout, margins
from numpy import zeros, arange, nan
try:
    import seaborn as sns
    sns.set(color_codes=True)
except ImportError:
    print ("""
Import of seaborn (matplotlib wrapper) failed. Continuing with plain matplotlib.

Installation:
    Using Anaconda:
        conda install seaborn
    Using pip:
        pip install seaborn
""")

try:
    from pandas import read_csv, isnull
except ImportError:
    raise ImportError("""
Import of pandas failed.

Installation:
    Using Anaconda:
        conda install pandas
    Using pip:
        pip install pandas
""")

def plot_temperature(tmin=None, tmax=None, ymin=None, ymax=None, show_image=True, month="January", SAVEFIG=None):
    """
    Generate a plot of the temperatures from dat/temperature.csv.

    Input:
        tmin:               Time in years to plot from.
        tmax:               Time in years to plot to.
        ymin:               Temperature in Celsius to plot from.
        ymax:               Temperature in Celsius to plot to.
        show_image:         Bool to determine if the image should be shown.
        month:              String with the month to plot temperatures for.
        SAVEFIG:            Name of file to save image to.
    """
    temperature_data = read_csv("dat/temperature.csv")
    plot(temperature_data["Year"], temperature_data[month])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year", "Temperature [Celsius]", "Average temperature for %s per year" % month)
    _show_and_save(show_image, SAVEFIG)


def plot_CO2(tmin=None, tmax=None, ymin=None, ymax=None, show_image=True, SAVEFIG=None):
    """
    Generate a plot of the CO2 emissions from dat/co2.csv.

    Input:
        tmin:               Time in years to plot from.
        tmax:               Time in years to plot to.
        ymin:               Carbon emissions to plot from.
        ymax:               Carbon emissions to plot to.
        show_image:         Bool to determine if the image should be shown.
        SAVEFIG:            Name of file to save image to.
    """
    co2_data = read_csv("dat/co2.csv")
    plot(co2_data["Year"], co2_data["Carbon"])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year", "Carbon [Gkg]","Carbon emissions in giga kilograms per year")
    _show_and_save(show_image, SAVEFIG)

def plot_CO2_emissions_per_country(lower_threshold=None, upper_threshold=None, year=2013, show_image=True, SAVEFIG=None):
    """
    Generate a plot of the CO2 emissions per country from dat/CO2_by_country.csv.

    Input:
        lower_threshold:    The minimum amount of emissions to plot from.
        upper_threshold:    The maximum amount of emissions to plot to.
        year:               The year to plot in.
        show_image:         Bool to determine if the image should be shown.
        SAVEFIG:            Name of file to save image to.
    """
    co2_country_data = read_csv("dat/CO2_by_country.csv", encoding="utf-8-sig")
    emission_data = co2_country_data[str(year)]

    # Check if upper and lower threshold is None
    upper_threshold = upper_threshold or max(emission_data.values) + 1e-10 # Add a small tolerance due to float-precision
    lower_threshold = lower_threshold or 0

    # Set all NAN-values to -1
    emission_data.values[isnull(emission_data.values)] = -1
    indices = (emission_data.values <= upper_threshold) & (emission_data.values >= lower_threshold)
    x_indices = arange(len(co2_country_data[u'"Country Name"'].values[indices]))

    if len(x_indices) >= 40:
        figure(figsize=(len(x_indices)*0.4 + 2, 9))
    else:
        figure(figsize=(10, 9))

    bar(x_indices, emission_data.values[indices], align='center')
    xticks(x_indices, co2_country_data[u'"Country Name"'].values[indices], rotation='vertical')
    axhline(lower_threshold, linewidth=2, color='g', linestyle='dashed', label="Lower threshold")
    axhline(upper_threshold, linewidth=2, color='r', linestyle='dashed', label="Upper threshold")
    legend(loc='best')
    ylabel(co2_country_data["Indicator Name"].values[0])
    title("CO2 emissions per capita")
    tight_layout() # Fit country name labels in plot
    margins(x=0)
    _show_and_save(show_image, SAVEFIG)

def _set_plot_info(tmin, tmax, ymin, ymax, XLABEL, YLABEL, TITLE):
    """
    Set axis values, title and labels in plot.

    Input:
        tmin:               The minimum x-value.
        tmax:               The maximum x-value.
        ymin:               The minimum y-value.
        ymax:               The maximum y-value.
        XLABEL:             A string with the label on the x-axis.
        YLABEL:             A string with the label on the y-axis.
        TITLE:              A string with the title off the plot.
    """
    axis([tmin, tmax, ymin, ymax])
    xlabel(XLABEL)
    ylabel(YLABEL)
    title(TITLE)

def _show_and_save(show_image, SAVEFIG):
    """
    Save image and show to screen if the user wishes.

    Input:
        show_image:         A bool determining if the image should be shown on screen.
        SAVEFIG:            A filename to save plot to.
    """
    if SAVEFIG:
        savefig(SAVEFIG)
    if show_image:
        show()

if __name__ == '__main__':
    plot_CO2()
    plot_temperature()
    plot_CO2_emissions_per_country(upper_threshold=16, lower_threshold=8)
