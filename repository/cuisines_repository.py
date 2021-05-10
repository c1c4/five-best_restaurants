from repository.utils_repository import return_csv_as_list_of_dicts


class CuisinesRepository:
    def __init__(self):
        self.cuisines_list = self.load_cuisines_from_csv()
        self.cuisines_names_by_id = self.cuisines_by_id()

    @staticmethod
    def load_cuisines_from_csv() -> list:
        return return_csv_as_list_of_dicts('cuisines')

    def cuisines_by_id(self):
        """
        Create a dictionary based on a list of cuisines.
        :return: A dictionary of cuisines name by id
        """
        cuisine_dict_by_id = {}
        for cuisines in self.cuisines_list:
            cuisine_dict_by_id[cuisines.id] = cuisines.name

        return cuisine_dict_by_id

    def load_cuisine_by_name(self, name):
        """
        Find in a list of cuisines by name

        :parameter name: cuisine user want to search could by exact or part of the name

        :return: Return a object of type Cuisine
        """
        filtered_list = [cus for cus in self.cuisines_list if cus.name.lower().__contains__(name.lower())]

        if len(filtered_list) > 0:
            return filtered_list[0]

    def load_cuisine_by_id(self, id_cuisine):
        """
        Find in a cuisine by id in dictionary of cuisine by id

        :parameter id_cuisine: user want to search

        :return: Return a object of type Cuisine
        """
        return self.cuisines_names_by_id[id_cuisine]
