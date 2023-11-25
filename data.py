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
dataset = graphs.readCSV(path_to_csv)
date_lis = graphs.get_date_lis()
date_lis = graphs.date_to_list(dataset, date_lis)

# getting data
graphs.add_all_data(dataset, date_lis)
calm_lis = graphs.get_calm()
relax_lis = graphs.get_relax()
energy_lis = graphs.get_energy()

print(date_lis)
print(calm_lis)
print(relax_lis)
print(energy_lis)

dataframe = pd.DataFrame({DATE:date_lis,
                          RELAX:relax_lis,
                          ENERGY:energy_lis,
                          CALM:calm_lis})


property_chart = {"type": "bar",
                  "x": DATE,
                  "y[1]": RELAX,
                  "y[2]": ENERGY,
                  "y[3]": CALM,
                  "color[1]": COOLPINK,
                  "color[2]": COOLGREEN,
                  "color[3]": PASTELYELLOW,
                 }

'''
page = """
# Analytics
<|{dataframe}|chart|properties={property_chart}|>

"""

Gui(page).run(run_browser=False, stylekit=stylekit)
'''