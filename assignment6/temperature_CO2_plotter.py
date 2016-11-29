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
    temperature_data = read_csv("dat/temperature.csv")
    plot(temperature_data["Year"], temperature_data[month])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year", "Temperature [Celsius]", "Average temperature for %s per year" % month)
    _show_and_save(show_image, SAVEFIG)


def plot_CO2(tmin=None, tmax=None, ymin=None, ymax=None, show_image=True, SAVEFIG=None):
    co2_data = read_csv("dat/co2.csv")
    plot(co2_data["Year"], co2_data["Carbon"])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year", "Carbon [Gkg]","Carbon emissions in giga kilograms per year")
    _show_and_save(show_image, SAVEFIG)

def plot_CO2_emissions_per_country(lower_threshold=None, upper_threshold=None,
                                   year=2013, show_image=True, SAVEFIG=None):
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
    axis([tmin, tmax, ymin, ymax])
    xlabel(XLABEL)
    ylabel(YLABEL)
    title(TITLE)

def _show_and_save(show_image, SAVEFIG=None):
    if SAVEFIG:
        savefig(SAVEFIG)
    if show_image:
        show()

if __name__ == '__main__':
    plot_CO2()
    plot_temperature()
    plot_CO2_emissions_per_country(upper_threshold=16, lower_threshold=8)
