from pandas import read_csv
from matplotlib.pylab import plot, show, axis, savefig, xlabel, ylabel, title


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

    def plot_CO2_emissions_per_country(self, upper_threshold=None, lower_threshold=None):
        co2_country_data = read_csv("dat/CO2_by_country.csv")
        print (co2_country_data)

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
    pcd.plot_CO2_emissions_per_country()
