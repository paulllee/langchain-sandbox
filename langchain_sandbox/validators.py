from typing import Union


class GroceriesValidator:
    def __init__(self, groceries: dict[str, dict[str, Union[float, int]]]) -> None:
        self.groceries: dict[str, dict[str, Union[float, int]]] = groceries
        self.error: str = ""

    def validate(self) -> bool:
        return self._are_grocery_values_valid()

    def _are_grocery_values_valid(self) -> bool:
        error: str = "Invalid {value} for {grocery_name}. Ask the user for a valid one."
        for grocery_name, grocery_values in self.groceries.items():
            if grocery_values.get("quantity", 0) <= 0:
                self.error: str = error.format(value="quantity", grocery_name=grocery_name)
                return False
            if grocery_values.get("price", -1.0) < 0.0:
                self.error: str = error.format(value="price", grocery_name=grocery_name)
                return False
        return True
