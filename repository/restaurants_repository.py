from typing import Iterable

from model.restaurant import Restaurant
from repository.utils_repository import return_csv_as_list_of_dicts


class RestaurantsRepository:
    restaurants_list: Iterable[Restaurant]

    def __init__(self):
        self.restaurants_list = self.load_restaurants_from_csv()

    @staticmethod
    def load_restaurants_from_csv() -> Iterable[Restaurant]:
        return return_csv_as_list_of_dicts('restaurants')

    def load_restaurants_by_params(self, name, customer_rating, distance, price, cuisine_id):
        filtered_list = []
        if name is not None:
            filtered_list = [res for res in self.restaurants_list if res.name.lower().__contains__(name.lower())]

        if customer_rating is not None:
            if len(filtered_list) == 0:
                filtered_list = [res for res in self.restaurants_list if res.customer_rating >= customer_rating]
            else:
                filtered_list = [res for res in filtered_list if res.customer_rating >= customer_rating]

        if distance is not None:
            if len(filtered_list) == 0:
                filtered_list = [res for res in self.restaurants_list if res.distance <= distance]
            else:
                filtered_list = [res for res in filtered_list if res.distance <= distance]

        if price is not None:
            if len(filtered_list) == 0:
                filtered_list = [res for res in self.restaurants_list if res.price <= price]
            else:
                filtered_list = [res for res in filtered_list if res.price <= price]

        if cuisine_id is not None:
            if len(filtered_list) == 0:
                filtered_list = [res for res in self.restaurants_list if res.cuisine_id == cuisine_id]
            else:
                filtered_list = [res for res in filtered_list if res.cuisine_id == cuisine_id]

        return filtered_list
