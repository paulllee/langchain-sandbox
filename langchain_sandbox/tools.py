from typing import Union

from langchain import tools

from langchain_sandbox import schemas, validators


@tools.tool(args_schema=schemas.GroceriesInput)
def get_total_cost_and_summary(groceries: dict[str, Union[float, int]]) -> str:
    """
    Returns the total cost of all grocery items in a valid arg structure
    """
    validator: validators.GroceriesValidator = validators.GroceriesValidator(groceries)
    if not validator.validate():
        return validator.error

    total_cost: float = 0.0
    max_total_cost: dict[str, Union[list[str], float]] = {"name": [], "cost": 0.0}
    for grocery_name, grocery_values in groceries.items():
        total_cost += (cost := round(grocery_values["price"] * grocery_values["quantity"], 2))
        if cost > max_total_cost["cost"]:
            max_total_cost["name"] = [grocery_name]
            max_total_cost["cost"] = cost
        elif cost == max_total_cost["cost"]:
            max_total_cost["name"].append(grocery_name)

    return f"The total cost of all items is {total_cost}."
