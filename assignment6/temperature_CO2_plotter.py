from pandas import read_csv
from matplotlib.pylab import plot, show, axis, savefig, xlabel, ylabel, title, bar, xticks, axhline, legend
from numpy import zeros, arange



def plot_temperature(tmin=None, tmax=None, ymin=None, ymax=None,
                     show_image=True, month="January", SAVEFIG=None):
    temperature_data = read_csv("dat/temperature.csv")
    plot(temperature_data["Year"], temperature_data[month])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year", "Temperature [Celsius]",
                   "Average tempature for %s per year" % month)
    _show_and_save(show_image, SAVEFIG)


def plot_CO2(tmin=None, tmax=None, ymin=None, ymax=None, show_image=True,
             SAVEFIG=None):
    co2_data = read_csv("dat/co2.csv")
    plot(co2_data["Year"], co2_data["Carbon"])
    _set_plot_info(tmin, tmax, ymin, ymax, "Year",
                   "Carbon [Gkg]","Carbon emissions in giga kilograms per year")
    _show_and_save(show_image, SAVEFIG)

def plot_CO2_emissions_per_country(lower_threshold=None, upper_threshold=None,
                                   year=2013, show_image=True SAVEFIG=None):
    co2_country_data = read_csv("dat/CO2_by_country.csv")
    emission_data = co2_country_data[str(year)]
    # Add a small tolerance due to float-precision
    upper_threshold = upper_threshold or max(emission_data.values) + 1e-10
    lower_threshold = lower_threshold or 0
    indices = (emission_data.values <= upper_threshold) & \
              (emission_data.values >= lower_threshold)
    x_indices = arange(len(co2_country_data["Country Code"].values[indices]))
    bar(x_indices, emission_data.values[indices], align='center')
    xticks(x_indices, co2_country_data["Country Code"].values[indices],
           rotation='vertical')
    axhline(lower_threshold, linewidth=2, color='g', label="Lower threshold")
    axhline(upper_threshold, linewidth=2, color='r', label="Upper threshold")
    legend(loc='best')
    ylabel(co2_country_data["Indicator Name"].values[0])
    title("CO2 emissions per capita")
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
    plot_CO2_emissions_per_country(upper_threshold=10, lower_threshold=8)
