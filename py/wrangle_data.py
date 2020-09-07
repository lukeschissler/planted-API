import pandas
import os
import sys

os.chdir('/Users/lukeschissler/documents/Github/node_react/py')

plant_df = pandas.read_csv("plant-data.csv")

state = sys.argv[1]
invasive = sys.argv[2]
protein = sys.argv[3]

"""
state='undefined'
invasive='undefined'
protein='High'
"""

def filter_by_state(df, state):
    return df.loc[df['State and Province'].str.contains(state)]

def filter_by_protein(df, level):
    # Options: Low, Medium, High
    if level == 'high':
        level = 'High'
    if level == 'low':
        level = 'Low'
    if level == 'medium':
        level = 'Medium'
    return df.loc[df['Protein Potential'] == level]

def filter_by_invasive(df):
    return df.loc[df["Invasive"].notna()]

def filter_by_BNS(df):
    notna_df = df.loc[df["Berry/Nut/Seed Product"].notna()]
    return notna_df.loc[notna_df["Berry/Nut/Seed Product"] == 'Yes']

def to_JSON(df):
    return df.to_json(orient="records")

if invasive == '1':
    plant_df = filter_by_invasive(plant_df)

if state != 'undefined':
    plant_df = filter_by_state(plant_df, state)

if protein != 'undefined':
    plant_df = filter_by_protein(plant_df, protein)

print(to_JSON(plant_df.head()))