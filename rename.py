import csv

import os

cwd = os.getcwd()

import requests

def rename_file(row):
    name = row["name"] + '.jpg'
    new = row["new"] + '.jpg'
    print(f"renaming {name} to {new}")
    if os.path.exists(name):
        os.rename(name, new)
    else:
        print(name + " does not exist")


with open('rename_list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        rename_file(row)
