from pandas import read_csv
from matplotlib.pylab import plot, show, axis, savefig, xlabel, ylabel, title, bar, xticks, axhline, legend
from numpy import zeros, arange


class PlotClimateData:

    def __init__(self, tmin=None, tmax=None, ymin=None, ymax=None, SAVEFIG=None, show_image=True):
        self.tmin = tmin
        self.tmax = tmax
        self.ymin = ymax
        self.ymax = ymax
        self.SAVEFIG = SAVEFIG
        self.show_image = show_image

    def plot_temperature(self, month="January"):
        temperature_data = read_csv("dat/temperature.csv")
        plot(temperature_data["Year"], temperature_data[month])
        self._set_plot_info("Year", "Temperature [Celsius]", "Average tempature for %s per year" % month)


    def plot_CO2(self):
        co2_data = read_csv("dat/co2.csv")
        plot(co2_data["Year"], co2_data["Carbon"])
        self._set_plot_info("Year", "Cabon [Gkg]","Cabon emissions in giga kilograms per year")

    def plot_CO2_emissions_per_country(self, lower_threshold=None, upper_threshold=None, year=2013):
        co2_country_data = read_csv("dat/CO2_by_country.csv")
        emission_data = co2_country_data[str(year)]
        upper_threshold = upper_threshold or max(emission_data.values) + 1e-10 # Add a small tolerance due to float-precision
        lower_threshold = lower_threshold or 0
        indices = (emission_data.values <= upper_threshold) & (emission_data.values >= lower_threshold)
        x_indices = arange(len(co2_country_data["Country Code"].values[indices]))
        bar(x_indices, emission_data.values[indices], align='center')
        xticks(x_indices, co2_country_data["Country Code"].values[indices], rotation='vertical')
        axhline(lower_threshold, linewidth=2, color='g', label="Lower threshold")
        axhline(upper_threshold, linewidth=2, color='r', label="Upper threshold")
        legend(loc='best')
        show()

    def _set_plot_info(self, XLABEL, YLABEL, TITLE):
        axis([self.tmin, self.tmax, self.ymin, self.ymax])
        xlabel(XLABEL)
        ylabel(YLABEL)
        title(TITLE)
        if self.SAVEFIG:
            savefig(self.SAVEFIG)
        if self.show_image:
            show()

if __name__ == '__main__':
    pcd = PlotClimateData()
    #pcd.plot_temperature()
    #pcd.plot_CO2()
    pcd.plot_CO2_emissions_per_country(upper_threshold=10, lower_threshold=8)
