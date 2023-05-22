import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.temp_dict = {}

        self.read_csv()

    def read_csv(self):
        with open(self.source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                self.process_rows_from_file(row)

            self.finalize_all_dishes_instantiated()

    def process_rows_from_file(self, row):
        dish_name, dish_price, ingredient_name, ingredient_quantity = row

        dish_price = float(dish_price)
        ingredient_quantity = int(ingredient_quantity)

        dish = self.get_or_create_dish(dish_name, dish_price)

        self.add_ingredient_to_dish(dish, ingredient_name, ingredient_quantity)

    def get_or_create_dish(self, dish_name, dish_price):
        if dish_name in self.temp_dict:
            return self.temp_dict[dish_name]
        else:
            dish = Dish(dish_name, dish_price)
            self.temp_dict[dish_name] = dish
            return dish

    def add_ingredient_to_dish(
        self, dish, ingredient_name, ingredient_quantity
    ):
        ingredient = Ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def finalize_all_dishes_instantiated(self):
        self.dishes = set(self.temp_dict.values())
