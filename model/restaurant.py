from dataclasses import dataclass


@dataclass
class Restaurant:
    name: str
    customer_rating: float
    distance: float
    price: float
    cuisine_id: int
    cuisine_name: any
