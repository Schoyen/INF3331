from pandas import read_csv
from matplotlib.pylab import plot, show, axis, savefig, xlabel, ylabel, title

def plot_temperature(month="January", tmin=None, tmax=None, ymin=None, ymax=None, SAVEFIG=None):
    temperature_data = read_csv("dat/temperature.csv")
    plot(temperature_data["Year"], temperature_data[month])
    axis([tmin, tmax, ymin, ymax])
    xlabel("Year")
    ylabel("Temperature [Celsius]")
    title("Average tempature for %s per year" % month)
    if SAVEFIG:
        savefig(SAVEFIG)
    show()

def plot_CO2(tmin=None, tmax=None, ymin=None, ymax=None, SAVEFIG=None):
    co2_data = read_csv("dat/co2.csv")
    plot(co2_data["Year"], co2_data["Carbon"])
    axis([tmin, tmax, ymin, ymax])
    xlabel("Year")
    ylabel("Carbon [Gkg]")
    title("Cabon emissions in giga kilograms per year")
    if SAVEFIG:
        savefig(SAVEFIG)
    show()

if __name__ == '__main__':
    plot_temperature()
    plot_CO2()
