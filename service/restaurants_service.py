from repository.cuisines_repository import CuisinesRepository
from repository.restaurants_repository import RestaurantsRepository


def get_restaurants(name=None, customer_rating=None, distance=None, price=None, cuisine_name=None) -> list:
    """
    Method that will find the cuisine_id by the name of cuisine.
    Filter all restaurants accordingly to the params.
    Sorted list with the criteria distance -> customer_rating -> price -> custom
    If have more than 5 results just resturn the first 5.

    :param name: Restaurants name
    :param customer_rating: Evaluation about the restaurant
    :param distance: Distance between the restaurant and the building you are
    :param price: Price of the plate per person
    :param cuisine_name: Type of cuisine e.g: Chinese
    :return: A sorted list only 5 or less. If don't find anything
    """
    cuisine_id = None

    if cuisine_name:
        cuisine = CuisinesRepository().load_cuisine_by_name(cuisine_name)
        if cuisine:
            cuisine_id = cuisine.id

    list_restaurants = RestaurantsRepository().load_restaurants_by_params(name, customer_rating, distance, price,
                                                                          cuisine_id)

    size = len(list_restaurants)
    if size == 0:
        return []
    elif size == 1:
        return list_restaurants
    else:
        sorted_restaurants = sort_restaurants(list_restaurants, 'distance')
        reduced_list_restaurants = sorted_restaurants if len(sorted_restaurants) <= 5 else sorted_restaurants[:5]
        for red in reduced_list_restaurants:
            red.cuisine_name = CuisinesRepository().load_cuisine_by_id(red.cuisine_id)

        return reduced_list_restaurants


def sort_restaurants(list_restaurants: list, sort_method):
    """
    A recursive method will sort a list of restaurants if have more than one item.
    Based on the criteria distance -> if we find 2 items with the same distance we call again
    the method and change the sorted method to customer_rating and so on until he get the custom sorted

    :param list_restaurants: list of restaurants
    :param sort_method: what type of sorted
    :return: list of restaurant sorted by distance or customer_rating or price or custom
    """
    if sort_method == 'distance':
        filtered_restaurants = sorted(list_restaurants, key=lambda res: res.distance)
        first_restaurant = filtered_restaurants[0]
        equal_matches = len([res for res in filtered_restaurants if res.distance == first_restaurant.distance]) > 1
        if equal_matches:
            return sort_restaurants(filtered_restaurants, 'customer_rating')

    if sort_method == 'customer_rating' or sort_method == 'custom':
        filtered_restaurants = sorted(list_restaurants, key=lambda res: res.customer_rating, reverse=True)
        if sort_method != 'custom':
            first_restaurant = filtered_restaurants[0]
            equal_matches = len(
                [res for res in filtered_restaurants if res.customer_rating == first_restaurant.customer_rating]
            ) > 1
            if equal_matches:
                return sort_restaurants(filtered_restaurants, 'price')

    if sort_method == 'price':
        filtered_restaurants = sorted(list_restaurants, key=lambda res: res.price)
        first_restaurant = filtered_restaurants[0]
        equal_matches = len(
            [res for res in filtered_restaurants if res.price == first_restaurant.price]
        ) > 1
        if equal_matches:
            return sort_restaurants(filtered_restaurants, 'custom')

    return filtered_restaurants
