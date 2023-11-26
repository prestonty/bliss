from taipy import Gui
import graphs
import pandas as pd


# constants
RELAX = "Relaxing"
CALM = "Calming"
ENERGY = "Energizing"
BREAKTYPE = "Break"
DATE = "Date"
COOLPINK = "#f8b4ce"
COOLGREEN = "#a2c9ba"
PASTELYELLOW = "#f8ecb4"

path_to_csv = "test.csv"
# getting list of dates

# getting data
def refresh_data():
    graphs.calmnum = 0
    graphs.relaxnum = 0
    graphs.energynum = 0

    graphs.date_lis = []
    graphs.relax_breaks = []
    graphs.calm_breaks = []
    graphs.energy_breaks = []
    dataset = graphs.readCSV(path_to_csv)
    date_lis = graphs.get_date_lis()
    date_lis = graphs.date_to_list(dataset, date_lis)
    dataset = graphs.readCSV(path_to_csv)
    date_lis = graphs.get_date_lis()
    date_lis = graphs.date_to_list(dataset, date_lis)
    graphs.add_all_data(dataset, date_lis)

calm_lis = graphs.get_calm()
relax_lis = graphs.get_relax()
energy_lis = graphs.get_energy()
date_lis = graphs.get_date_lis()


property_chart = {"type": "bar",
                  "x": DATE,
                  "rebuild": True,
                  "render": True,
                  "y[1]": RELAX,
                  "y[2]": ENERGY,
                  "y[3]": CALM,
                  "color[1]": COOLPINK,
                  "color[2]": COOLGREEN,
                  "color[3]": PASTELYELLOW,
                 }