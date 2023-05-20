import pytest
from models.dish import Dish
from models.ingredient import Ingredient


def test_dish():
    dish = Dish("Espaguete", 15.0)
    ingredient = Ingredient("Tomate")

    # Testa atributos básicos
    assert dish.name == "Espaguete"
    assert dish.price == 15.0
    assert dish.recipe == {}

    # Testa o método __repr__
    assert repr(dish) == "Dish('Espaguete', R$15.00)"

    # Testa o método __eq__
    assert dish == Dish("Espaguete", 15.0)
    assert dish != Dish("Pizza", 20.0)

    # Testa a igualdade de hash
    assert hash(dish) == hash(Dish("Espaguete", 15.0))
    assert hash(dish) != hash(Dish("Pizza", 20.0))

    # Testa se o método add_ingredient_dependency tem o comportamento esperado
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe == {ingredient: 2}

    # Testa se o método get_restrictions tem o comportamento esperado
    assert dish.get_restrictions() == ingredient.restrictions

    # Testa se o método get_ingredients tem o comportamento esperado
    assert dish.get_ingredients() == {ingredient}

    # Testa a exceção quando o preço é inválido
    with pytest.raises(TypeError):
        Dish("Salada", "dez")

    # Testa a exceção quando o preço é negativo
    with pytest.raises(ValueError):
        Dish("Feijoada", -10)
