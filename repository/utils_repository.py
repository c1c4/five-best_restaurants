import csv
import os
from pathlib import Path

from model.restaurant import Restaurant

from model.cuisine import Cuisine


def return_csv_as_list_of_dicts(csv_file):
    full_path = os.path.abspath(__file__)
    cwd = Path(full_path).parents[1]
    file = os.path.join(cwd, f'static', f'{csv_file}.csv')
    with open(file, newline='', encoding="utf-8") as csv_object:
        reader = csv.DictReader(csv_object)

        if csv_file == 'restaurants':
            return read_restaurants(reader)
        else:
            return read_cuisines(reader)


def read_restaurants(reader):
    list_of_restaurants = []
    for row in reader:
        list_of_restaurants.append(
            Restaurant(
                row.get('name'),
                float(row.get('customer_rating')),
                float(row.get('distance')),
                float(row.get('price')),
                int(row.get('cuisine_id')),
                None
            )
        )

    return list_of_restaurants


def read_cuisines(reader):
    list_of_cuisines = []
    for row in reader:
        list_of_cuisines.append(
            Cuisine(
                int(row.get('id')),
                row.get('name')
            )
        )

    return list_of_cuisines
