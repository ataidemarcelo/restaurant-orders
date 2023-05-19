from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 1
def test_ingredient():
    frango = Ingredient("frango")
    camarao = Ingredient("camarão")

    # Testa se o nome passado no construtor está correto no atributo name
    assert frango.name == "frango"
    assert camarao.name == "camarão"

    # Testa se o hash de dois ingredientes iguais são iguais
    assert hash(frango) == hash(Ingredient("frango"))

    # Testa se os hashs de ingredientes diferentes também sejam diferentes
    assert hash(frango) != hash(camarao)

    # Testa se o método __repr__ tem o comportamento esperado
    assert repr(frango) == "Ingredient('frango')"
    assert repr(camarao) == "Ingredient('camarão')"

    # Testa se o operador de igualdade identifique
    # ingredientes iguais e diferentes
    assert camarao == Ingredient("camarão")
    assert camarao != frango

    # Testa se o hash de dois ingredientes diferentes são diferentes
    assert hash(camarao) != hash(frango)

    # Testa se o atributo restrictions é preenchido corretamente
    assert camarao.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert frango.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
