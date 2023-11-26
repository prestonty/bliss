#graphs.py
import pandas as pd;

RELAX = "Relaxing"
CALM = "Calming"
ENERGY = "Energizing"
DATE = "Date"
BREAKTYPE = "Break"

calmnum = 0
relaxnum = 0
energynum = 0

date_lis = []
relax_breaks = []
calm_breaks = []
energy_breaks = []

#path_to_csv = getPath();
def readCSV(path_to_csv:str):
    dataset = pd.read_csv(path_to_csv)
    return dataset

# getters
def get_calm():
    return calm_breaks
def get_energy():
    return energy_breaks
def get_relax():
    return relax_breaks
def get_date_lis():
    return date_lis

def get_last_row(df_str):
    try:
        df = pd.read_csv(df_str)
        last_row = df.iloc[-1].tolist()
        add_last_row(last_row)
    except pd.errors.EmptyDataError:
        return None

def add_last_row(last_row):
    new_date = last_row[0]
    new_break = last_row[1]
    index = 0
    if new_date not in date_lis:
        date_lis.append(new_date)
        if new_break == RELAX:
            relax_breaks.append(1)
            calm_breaks.append(0)
            energy_breaks.append(0)
        elif new_break == CALM:
            relax_breaks.append(0)
            calm_breaks.append(1)
            energy_breaks.append(0)
        elif new_break == ENERGY:
            relax_breaks.append(0)
            calm_breaks.append(0)
            energy_breaks.append(1)
    else:
        for date in date_lis:
            if date == new_date:
                break
            index += 1
        if new_break == RELAX:
            relax_breaks[index] += 1
        elif new_break == CALM:
            calm_breaks[index] += 1
        elif new_break == ENERGY:
            energy_breaks[index] += 1

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
    filtered_df = df[df[DATE] == d]
    calmnum = 0
    relaxnum = 0
    energynum = 0

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
