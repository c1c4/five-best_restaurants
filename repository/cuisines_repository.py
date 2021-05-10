from repository.utils_repository import return_csv_as_list_of_dicts


class CuisinesRepository:
    def __init__(self):
        self.cuisines_list = self.load_cuisines_from_csv()
        self.cuisines_names_by_id = self.cuisines_by_id()

    @staticmethod
    def load_cuisines_from_csv() -> list:
        return return_csv_as_list_of_dicts('cuisines')

    def cuisines_by_id(self):
        cuisine_dict_by_id = {}
        for cuisines in self.cuisines_list:
            cuisine_dict_by_id[cuisines.id] = cuisines.name

        return cuisine_dict_by_id

    def load_cuisine_by_name(self, name):
        filtered_list = [cus for cus in self.cuisines_list if cus.name.lower().__contains__(name.lower())]

        if len(filtered_list) > 0:
            return filtered_list[0]

    def load_cuisine_by_id(self, id_cuisine):
        return self.cuisines_names_by_id[id_cuisine]
