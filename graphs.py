#graphs.py
import pandas as pd;

RELAX = "Relaxing"
CALM = "Calming"
ENERGY = "Energizing"
DATE = "Date"
BREAKTYPE = "Break"

date_lis = []
relax_breaks = []
calm_breaks = []
energy_breaks = []
latest_row = 0

#path_to_csv = getPath();
def readCSV(path_to_csv:str):
    dataset = pd.read_csv(path_to_csv)
    return dataset

'''
def get_data(path_to_csv: str):
    # pandas.read_csv() returns a pd.DataFrame
    dataset = pd.read_csv(path_to_csv)
    dataset[DATE] = pd.to_datetime(dataset[DATE])
    return dataset
'''

# getters
def get_calm():
    return calm_breaks
def get_energy():
    return energy_breaks
def get_relax():
    return relax_breaks
def get_date_lis():
    return date_lis

def date_to_list(df, dl):
    for d in df[DATE]:
        if d not in date_lis:
            dl.append(d)
    dl.sort()
    return dl

def add_all_data(df, dl):
    for d in dl:
        break_nums = set_breaks(df, d)
        calm_breaks.append(break_nums[0])
        relax_breaks.append(break_nums[1])
        energy_breaks.append(break_nums[2])

# def addBreak() add to csv
def set_breaks(df, d):
    calmnum = 0
    relaxnum = 0
    energynum = 0
    filtered_df = df[df[DATE] == d]

    for break_type in filtered_df[BREAKTYPE]:
        if break_type == CALM:
            calmnum += 1
        elif break_type == RELAX:
            relaxnum += 1
        elif break_type == ENERGY:
            energynum += 1
    if (calmnum == 0):
        calmnum = 0.001
    if (relaxnum == 0):
        relaxnum = 0.001
    if (energynum == 0):
        energynum = 0.001      
    return [calmnum, relaxnum, energynum]